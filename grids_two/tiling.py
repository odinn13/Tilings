from collections import defaultdict
from functools import partial, reduce
from itertools import chain
from array import array

from grids import Cell
from permuta import PermSet, Perm

from .misc import map_cell
from .obstruction import Obstruction
from .requirement import Requirement

__all__ = ("Tiling")


class Tiling():
    """Tiling class.

    Zero-indexed coordinates/cells from bottom left corner where the (x, y)
    cell is the cell in the x-th column and y-th row.
    """

    def __init__(self, point_cells=list(), positive_cells=list(),
                 possibly_empty=list(), obstructions=list(),
                 requirements=list(), remove_empty=True):
        # Set of the cells that have points in them
        self._point_cells = frozenset(point_cells)
        # Set of the cells that are positive, i.e. contain a point
        self._positive_cells = frozenset(positive_cells)
        # Set of possibly empty cells
        self._possibly_empty = frozenset(possibly_empty)
        # Set of obstructions
        self._obstructions = tuple(sorted(obstructions))
        # Set of requirement lists
        self._requirements = Tiling.sort_requirements(requirements)

        self._dimensions = None
        self.back_map = None

        # The cell sets should all be disjoint
        if self._positive_cells & self._possibly_empty:
            raise ValueError(("The set of positive cells and the set of "
                              "possibly empty cells should be disjoint."))
        if self._positive_cells & self._point_cells:
            raise ValueError(("The set of positive cells and the set of point"
                              " cells should be disjoint."))
        if self._possibly_empty & self._point_cells:
            raise ValueError(("The set of possibly empty cells and the set of "
                              "point cells should be disjoint."))

        # Check if positive_cells and possibly_empty cells cover the indices of
        # the obstructions.
        all_cells = (self._positive_cells |
                     self._possibly_empty |
                     self._point_cells)
        all_obstruction_cells = reduce(
            set.__or__, (set(ob.pos) for ob in self._obstructions), set())
        if not all_obstruction_cells <= all_cells:
            raise ValueError(("The set of positive cells and the set of "
                              "possibly empty cells should cover the cells "
                              "of the obstructions."))
        if not all(any(set(req.pos) for req in reqlist)
                   for reqlist in self._requirements):
            raise ValueError(("The set of positive cells and the set of "
                              "possibly empty cells should cover at least one"
                              "requirement in each requirement list."))

        self._minimize(remove_empty)
        self.dimensions

    def _minimize(self, remove_empty):
        """Minimizes the set of obstructions and for each single-point
        obstruction, removes the corresponding cell from the possibly empty
        set. Finally, removes all empty rows and columns and updates
        obstructions.
        """
        # Minimize the set of obstructions
        minimalobs = self._minimal_obs()
        # Minimize the set of requiriments
        minimalreqs = self._minimal_reqs()
        # Compute the single-point obstructions
        empty_cells = set(ob.is_point_obstr()
                          for ob in minimalobs if ob.is_point_obstr())
        # Compute the required points from the set of requirement lists
        #  required_points = set(chain.from_iterable(
        #      reduce(set.__and__, (set(req.pos) for req in reqlist))
        #      for reqlist in minimalreqs))

        # Remove the empty cells
        self._possibly_empty = frozenset(self._possibly_empty - empty_cells)
        if (self._positive_cells & empty_cells or
                self._point_cells & empty_cells):
            minimalobs.append(Obstruction.empty_obstruction)

        # Produce the mapping between the two tilings
        self._col_mapping, self._row_mapping = self._minimize_mapping()
        cell_map = partial(map_cell, self._col_mapping, self._row_mapping)

        # For backwards compatability only, will be removed in future.
        # TODO: Not use Cell, and convert the dictionary to Cell dictionary
        # when needed.
        self.back_map = {Cell(*cell_map(cell)): Cell(*cell)
                         for cell in (self.point_cells |
                                      self.possibly_empty |
                                      self._positive_cells)}

        if remove_empty:
            self._obstructions = tuple(
                sorted(ob.minimize(cell_map) for ob in minimalobs
                       if ob.is_point_obstr() is None))
            self._requirements = tuple(sorted(
                tuple(sorted(req.minimize(cell_map) for req in reqlist))
                for reqlist in minimalreqs))
            self._point_cells = frozenset(map(cell_map,
                                              self._point_cells))
            self._positive_cells = frozenset(map(cell_map,
                                                 self._positive_cells))
            self._possibly_empty = frozenset(map(cell_map,
                                                 self._possibly_empty))
        else:
            self._obstructions = tuple(ob for ob in minimalobs
                                       if ob.is_point_obstr() is None)
            self._requirements = tuple(
                tuple(sorted(req.minimize(cell_map) for req in reqlist)
                      for reqlist in minimalreqs))

    def _minimize_mapping(self):
        """Returns a pair of dictionaries, that map rows/columns to an
        equivalent set of rows/columns where empty ones have been removed. """
        all_cells = (self._positive_cells |
                     self._possibly_empty |
                     self._point_cells)

        if not all_cells:
            (i, j) = self.dimensions
            return ({x: 0 for x in range(i)},
                    {y: 0 for y in range(j)})

        col_set, row_set = map(set, zip(*all_cells))

        col_list, row_list = sorted(col_set), sorted(row_set)
        col_mapping = {x: actual for actual, x in enumerate(col_list)}
        row_mapping = {y: actual for actual, y in enumerate(row_list)}
        return (col_mapping, row_mapping)

    def _clean_isolated(self, obstruction):
        """Remove the isolated cells that are point cells or positive cells
        from all obstructions."""
        remove = [cell for cell in obstruction.isolated_cells()
                  if (cell in self._point_cells or
                      cell in self._positive_cells)]
        return obstruction.remove_cells(remove)

    def _minimal_obs(self):
        """Returns a new list of minimal obstructions from the obstruction set
        of self."""
        cleanobs = list()
        for ob in sorted(map(self._clean_isolated, self._obstructions)):
            add = True
            for co in cleanobs:
                if co in ob:
                    add = False
                    break
            if add:
                cleanobs.append(ob)
        return cleanobs

    def _minimal_reqs(self):
        """Returns a new set of minimal lists of requirements from the
        requirement set of self."""
        return self._requirements

    def to_old_tiling(self):
        import grids
        basi = defaultdict(list)
        for ob in self._obstructions:
            cell = ob.is_single_cell()
            if cell is not None:
                basi[cell].append(ob.patt)
        blocks = dict()
        for cell in self._point_cells:
            blocks[cell] = grids.Block.point
        for cell in self._possibly_empty:
            if cell not in basi:
                blocks[cell] = PermSet.avoiding(())
        for cell in self._positive_cells:
            if cell not in basi:
                blocks[cell] = grids.PositiveClass(PermSet.avoiding(()))
        for (cell, basis) in basi.items():
            if cell in self._positive_cells:
                blocks[cell] = grids.PositiveClass(PermSet.avoiding(basis))
            else:
                blocks[cell] = PermSet.avoiding(basis)
        return grids.Tiling(blocks)

    def compress(self, patthash=None):
        """Compresses the tiling by flattening the sets of cells into lists of
        integers which are concatenated together, every list preceeded by its
        size. The obstructions are compressed and concatenated to the list, as
        are the requirement lists."""
        result = []
        result.append(len(self.point_cells))
        result.extend(chain.from_iterable(self.point_cells))
        result.append(len(self.positive_cells))
        result.extend(chain.from_iterable(self.positive_cells))
        result.append(len(self.possibly_empty))
        result.extend(chain.from_iterable(self.possibly_empty))
        result.append(len(self.obstructions))
        result.extend(chain.from_iterable(ob.compress(patthash)
                                          for ob in self.obstructions))
        result.append(len(self.requirements))
        for reqlist in self.requirements:
            result.append(len(reqlist))
            result.extend(chain.from_iterable(req.compress(patthash)
                                              for req in reqlist))
        res = array('H', result)
        return res.tobytes()

    @classmethod
    def decompress(cls, arrbytes, patts=None):
        """Given a compressed tiling in the form of an 2-byte array, decompress
        it and return a tiling."""
        arr = array('H', arrbytes)
        offset = 1
        point_cells = [(arr[offset + 2*i], arr[offset + 2*i + 1])
                       for i in range(0, arr[offset - 1])]
        offset += 2 * arr[offset - 1] + 1
        positive_cells = [(arr[offset + 2*i], arr[offset + 2*i + 1])
                          for i in range(arr[offset - 1])]
        offset += 2 * arr[offset - 1] + 1
        possibly_empty = [(arr[offset + 2*i], arr[offset + 2*i + 1])
                          for i in range(arr[offset - 1])]
        offset += 2 * arr[offset - 1] + 1
        nobs = arr[offset - 1]
        obstructions = []
        for i in range(nobs):
            if patts:
                patt = patts[arr[offset]]
            else:
                patt = Perm.unrank(arr[offset])
            obstructions.append(Obstruction.decompress(
                arr[offset:offset + 2*(len(patt)) + 1], patts))
            offset += 2 * len(patt) + 1

        nreqs = arr[offset]
        offset += 1
        requirements = []
        for i in range(nreqs):
            reqlistlen = arr[offset]
            offset += 1
            reqlist = []
            for j in range(reqlistlen):
                if patts:
                    patt = patts[arr[offset]]
                else:
                    patt = Perm.unrank(arr[offset])
                reqlist.append(Requirement.decompress(
                    arr[offset:offset + 2*(len(patt)) + 1], patts))
                offset += 2 * len(patt) + 1
            requirements.append(reqlist)

        return cls(point_cells=point_cells,
                   positive_cells=positive_cells,
                   possibly_empty=possibly_empty,
                   obstructions=obstructions,
                   requirements=requirements)

    # Cell methods

    def delete_cell(self, cell):
        """Deletes a cell from every obstruction and returns a new tiling. The
        cell must be in the set of possibly empty cells."""
        if cell not in self._possibly_empty:
            raise ValueError("Cell {} is not deletable.".format(cell))
        newobs = [ob for ob in self._obstructions if not ob.occupies(cell)]
        return Tiling(self._point_cells,
                      self._positive_cells,
                      self._possibly_empty - {cell},
                      newobs,
                      self._requirements)

    def insert_cell(self, cell):
        """Inserts a cell into every obstruction and returns a new tiling. The
        cell must be in the set of possibly empty cells."""
        if cell not in self._possibly_empty:
            raise ValueError(
                "Cell {} is positive or not in the tiling.".format(cell))
        return Tiling(self._point_cells,
                      self._positive_cells | {cell},
                      self._possibly_empty - {cell},
                      self._obstructions,
                      self._requirements)

    def only_positive_in_row_and_column(self, cell):
        """Check if the cell is the only positive cell in row and column."""
        if cell not in self._positive_cells and cell not in self._point_cells:
            return False
        inrow = sum(1 for (x, y) in
                    chain(self._point_cells, self._positive_cells)
                    if y == cell[1])
        incol = sum(1 for (x, y) in
                    chain(self._point_cells, self._positive_cells)
                    if x == cell[0])
        return (inrow == 1 and incol == 1)

    def only_positive_in_row(self, cell):
        """Check if the cell is the only positive cell in row."""
        inrow = sum(1 for (x, y) in
                    chain(self._point_cells, self._positive_cells)
                    if y == cell[1])
        return inrow == 1

    def only_positive_in_col(self, cell):
        """Check if the cell is the only positive cell in column."""
        incol = sum(1 for (x, y) in
                    chain(self._point_cells, self._positive_cells)
                    if x == cell[0])
        return incol == 1

    def only_cell_in_col(self, cell):
        incol = sum(1 for (x, y) in
                    chain(self._point_cells,
                          self._positive_cells,
                          self._possibly_empty)
                    if x == cell[0])
        return incol == 1

    def only_cell_in_row(self, cell):
        inrow = sum(1 for (x, y) in
                    chain(self._point_cells,
                          self._positive_cells,
                          self._possibly_empty)
                    if y == cell[1])
        return inrow == 1

    def cells_in_row(self, row):
        """Return all point, positive and possibly empty cells in row."""
        return [(x, y) for (x, y) in chain(self._point_cells,
                                           self._positive_cells,
                                           self._possibly_empty) if y == row]

    def cells_in_col(self, col):
        """Return all point, positive and possibly empty cells in column."""
        return [(x, y) for (x, y) in chain(self._point_cells,
                                           self._positive_cells,
                                           self._possibly_empty) if x == col]

    @staticmethod
    def sort_requirements(requirements):
        return tuple(sorted(tuple(sorted(reqlist))
                            for reqlist in requirements))

    # Symmetries
    def _transform(self, transf, gptransf):
        return Tiling(point_cells=map(transf, self.point_cells),
                      positive_cells=map(transf, self.positive_cells),
                      possibly_empty=map(transf, self.possibly_empty),
                      obstructions=(gptransf(ob) for ob in self.obstructions),
                      requirements=([gptransf(req) for req in reqlist]
                                    for reqlist in self.requirements))

    def reverse(self):
        """ |
        Reverses the tiling within its boundary. Every cell and obstruction
        gets flipped over the vertical middle axis."""
        def reverse_cell(cell):
            return (self.dimensions[0] - cell[0] - 1, cell[1])
        return self._transform(
            reverse_cell,
            lambda ob: ob.reverse(reverse_cell))

    def complement(self):
        """ -
        Flip over the horizontal axis.  """
        def complement_cell(cell):
            return (cell[0], self.dimensions[1] - cell[1] - 1)
        return self._transform(
            complement_cell,
            lambda ob: ob.complement(complement_cell))

    def inverse(self):
        """ /
        Flip over the diagonal"""
        def inverse_cell(cell):
            return (cell[1], cell[0])
        return self._transform(
            inverse_cell,
            lambda ob: ob.inverse(inverse_cell))

    def antidiagonal(self):
        """ \\
        Flip over the anti-diagonal"""
        def antidiagonal_cell(cell):
            return (self.dimensions[1] - cell[1] - 1,
                    self.dimensions[0] - cell[0] - 1)
        return self._transform(
            antidiagonal_cell,
            lambda ob: ob.antidiagonal(antidiagonal_cell))

    def rotate270(self):
        """Rotate 270 degrees"""
        def rotate270_cell(cell):
            return (self.dimensions[1] - cell[1] - 1,
                    cell[0])
        return self._transform(
            rotate270_cell,
            lambda ob: ob.rotate270(rotate270_cell))

    def rotate180(self):
        """Rotate 180 degrees"""
        def rotate180_cell(cell):
            return (self.dimensions[0] - cell[0] - 1,
                    self.dimensions[1] - cell[1] - 1)
        return self._transform(
            rotate180_cell,
            lambda ob: ob.rotate180(rotate180_cell))

    def rotate90(self):
        """Rotate 90 degrees"""
        def rotate90_cell(cell):
            return (cell[1],
                    self.dimensions[0] - cell[0] - 1)
        return self._transform(
            rotate90_cell,
            lambda ob: ob.rotate90(rotate90_cell))

    #
    # Properties and getters
    #

    def is_empty(self):
        return any(ob.is_empty() for ob in self)

    @property
    def point_cells(self):
        return self._point_cells

    @property
    def total_points(self):
        return len(self._point_cells)

    @property
    def possibly_empty(self):
        return self._possibly_empty

    @property
    def positive_cells(self):
        return self._positive_cells

    @property
    def total_positive(self):
        return len(self._positive_cells)

    @property
    def obstructions(self):
        return self._obstructions

    @property
    def total_obstructions(self):
        return len(self._obstructions)

    @property
    def requirements(self):
        return self._requirements

    @property
    def total_requirements(self):
        return len(self._requirements)

    @property
    def dimensions(self):
        if self._dimensions is None:
            all_cells = (self._positive_cells |
                         self._possibly_empty |
                         self._point_cells)

            rows = set(x for (x, y) in all_cells | all_cells)
            cols = set(y for (x, y) in all_cells | all_cells)
            if not rows and not cols:
                self._dimensions = (1, 1)
                return self._dimensions
            self._dimensions = (max(rows) - min(rows) + 1,
                                max(cols) - min(cols) + 1)
        return self._dimensions

    #
    # Dunder methods
    #

    def __hash__(self):
        return (hash(self._point_cells) ^ hash(self._possibly_empty) ^
                hash(self._positive_cells) ^ hash(self._obstructions) ^
                hash(self._requirements))

    def __eq__(self, other):
        return (self.point_cells == other.point_cells and
                self.possibly_empty == other.possibly_empty and
                self.positive_cells == other.positive_cells and
                self.obstructions == other.obstructions,
                self.requirements == other.requirements)

    def __len__(self):
        return len(self._obstructions)

    def __repr__(self):
        format_string = ("Tiling(point_cells={}, "
                         "positive_cells={}, "
                         "possibly_empty={}, "
                         "obstructions={}, "
                         "requirements={})")
        return format_string.format(self.point_cells,
                                    self.positive_cells,
                                    self.possibly_empty,
                                    self.obstructions,
                                    self.requirements)

    def __str__(self):
        return "\n".join([
            "Point cells: " + str(self._point_cells),
            "Positive cells: " + str(self._positive_cells),
            "Possibly empty cells: " + str(self._possibly_empty),
            "Obstructions: " + ", ".join(list(map(repr, self._obstructions))),
            "Requirements: [[" + "], [".join(
                list(map(lambda x: ", ".join(list(map(repr, x))),
                         self._requirements))) + "]]"])

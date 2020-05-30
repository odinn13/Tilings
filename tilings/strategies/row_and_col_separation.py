"""
The row and column separation strategy. The details of the algorithm can be
found in the algorithms folder.
"""
from typing import Dict, Optional, Tuple

from comb_spec_searcher import DisjointUnionStrategy
from tilings import GriddedPerm, Tiling
from tilings.algorithms import RowColSeparation

__all__ = ["RowColumnSeparationStrategy"]


Cell = Tuple[int, int]
CellMap = Dict[Cell, Cell]


class RowColumnSeparationStrategy(DisjointUnionStrategy[Tiling, GriddedPerm]):
    """
    An inferral strategy that tries to separate cells in rows and columns.
    """

    _cell_maps: Dict[Tiling, Tuple[CellMap, CellMap]] = {}

    def __init__(self):
        super().__init__(
            ignore_parent=True, inferrable=True, possibly_empty=False, workable=True,
        )

    def forward_cell_map(self, tiling: Tiling) -> CellMap:
        return self._get_cell_maps(tiling)[0]

    def backward_cell_map(self, tiling: Tiling) -> CellMap:
        return self._get_cell_maps(tiling)[1]

    def _get_cell_maps(self, tiling: Tiling) -> Tuple[CellMap, CellMap]:
        res = self._cell_maps.get(tiling)
        if res is None:
            forward_cell_map = self.row_col_sep_algorithm(tiling).get_cell_map()
            backward_cell_map = {y: x for x, y in forward_cell_map.items()}
            self._cell_maps[tiling] = forward_cell_map, backward_cell_map
        else:
            forward_cell_map, backward_cell_map = res
        return forward_cell_map, backward_cell_map

    def decomposition_function(self, tiling: Tiling) -> Tuple[Tiling, ...]:
        """Return the separated tiling if it separates, otherwise None."""
        rcs = self.row_col_sep_algorithm(tiling)
        if rcs.separable():
            return (rcs.separated_tiling(),)

    @staticmethod
    def row_col_sep_algorithm(tiling: Tiling) -> RowColSeparation:
        """Return the algorithm class using tiling."""
        return RowColSeparation(tiling)

    @staticmethod
    def formal_step() -> str:
        """Return formal step."""
        return "row and column separation"

    def backward_map(
        self,
        tiling: Tiling,
        gps: Tuple[Optional[GriddedPerm], ...],
        children: Optional[Tuple[Tiling, ...]] = None,
    ) -> GriddedPerm:
        """This method will enable us to generate objects, and sample. """
        if children is None:
            children = self.decomposition_function(tiling)
        gp = gps[0]
        assert gp is not None
        backmap = self.backward_cell_map(tiling)
        return gp.apply_map(backmap.__getitem__)

    def forward_map(
        self,
        tiling: Tiling,
        gp: GriddedPerm,
        children: Optional[Tuple[Tiling, ...]] = None,
    ) -> Tuple[GriddedPerm]:
        """This function will enable us to have a quick membership test."""
        if children is None:
            children = self.decomposition_function(tiling)
        forwardmap = self.forward_cell_map(tiling)
        gp = gp.apply_map(forwardmap.__getitem__)
        return (gp,)

    def __str__(self) -> str:
        return "row and column separation"

    def __repr__(self) -> str:
        return "RowColumnSeparationStrategy()"

    @classmethod
    def from_dict(cls, d) -> "RowColumnSeparationStrategy":
        return cls()
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- introduced isolation levels to the fusion strategy
- added the `one_cell_only` option to `CellInsertionFactory`
- `remove_components_from_assumptions` method to `Tiling`
- `DetectComponentsStrategy` which removes cells from assumptions
   which are actual components. This replaces the need for the
   `SplittingStrategy` in component fusion packs.
- added equation generators to `FusionStrategy` for the case where one or both
   sides are positive

### Changed
- insertion packs now use the `one_cell_only` option, and no longer use
  `RequirementCorroborationFactory`
- the `get_eq_symbol` and `get_op_symbol` are moved to `Strategy` rather than
  `Constructor`
- the `GriddedPermsOnTiling` algorithm was changed to build from minimal
  gridded perms in a breadth first manner. This is also include an option to
  limit the number of points placed on the minimal gridded perms.

### Fixed
- untracked constructors raise `NotImplementedError`
- forbid fusing a region containing a `TrackingAssumption` and a
  `ComponentAssumption`
- a tiling factors if a `ComponentAssumption` if the components of the region
  split into the factors
- only fuse non-empty regions to avoid creating unintentional rules a -> b
  where a and b are equivalent
- remove duplicate assumptions in the `AddAssumptionsStrategy`
- `Tiling.from_dict` will make a `Tiling` with no assumptions if the
  `assumptions` key is not in the dictionary.
- a factor with interleaving strategy has `inferrable=True`
- a factor with interleaving strategy return a normal factor strategy when
  there's no interleaving going on.
- removed the length argument to the `insertion_point_placements` pack which
  was not implemented, and thus raising an error.
- Bug that occurred when factoring the empty tiling


## [2.2.0] - 2020-07-08
### Added
- add the `can_be_equivalent` methods to `AddAssumptionsStrategy`,
  `SplittingStrategy`, and `FusionStrategy`.
- added a `get_assumption` method to `Tiling`

### Changed
- the `Factor` algorithm will now factor `TrackingAssumptions` if they span
  multiple factors of the tiling. This means that the `SplittingStrategy` is
  removed from the tracked `StrategyPack`. It does not factor
  `ComponentAssumptions`, so using this strategy still requires the
  `SplittingStrategy`.

### Fixed
- remove empty assumptions when creating extra parameters in `FusionStrategy`
- the method `Tiling.get_genf` returns the Catalan generating function for Av(123).
- correct the generating function equations for `SplittingStrategy`

### Removed
- Removed optional arguments from the `from_bytes` method on `Tiling`

## [2.1.0] - 2020-06-29
### Added
- add a new `AddAssumptionStrategy` which adds an assumption to a tiling.
  In practice, when expanding a class, we actually remove an assumption to
  determine which rules to add.
- the `get_equations` method is now implemented for the strategies
  `AddAssumptionStrategy`, `SplittingStrategy`, and `FusionStrategy`.
- the `extra_paramters` method was implemented for symmetry strategies,
  allowing these to be used when enumerating tracked trees.
- Add the `InsertionEncodingVerificationStrategy` which verifies n x 1 and
  1 x n tilings which have a regular topmost or bottommost insertion encoding.
- Added the `SumComponentAssumption` and `SkewComponentAssumption` giving the
  ability to track specifications using component fusion.
- add partial flag to `insertion_point_placements` and
  `insertion_row_and_col_placements`
- Allow fusing rows and columns which are positive on either or both sides.
- The tracking of interleaving factors is implemented, including the poly time
  algorithm. This includes the new strategy `AddInterleavingAssumptionFactory`
  which adds the assumptions required in order to enumerate when performing
  an interleaving factor strategy.
- The `TileScopePack` has a new method `make_interleaving` which by will change
  any factor strategy in the pack to allow interleaving. The default setting is
  for tracked, and so the assumption strategies are also added. This can be
  turned off with the flag `tracked=False`.
- The `possible_parameters` method on `Tiling` allowing for sanity checking
  specifications with multiple variables.
- `InsertionEncodingVerificationStrategy` was added to verification expansion
  packs.
- `forward_map_assumption` method on `Tiling`.

### Changed
- The definition of a local `TrackingAssumption` in `LocalEnumeration` now says
  it is local if every gp in it is local (before it was they all used the same
  single cell).
- the default in `LocalVerificationStrategy` is now `no_factors=False`.

### Fixed
- untracked fusion packs don't add assumption strategies
- the length parameter for `all_the_strategies` is passed correctly to the
  requirement insertion strategy.
- use fusion on positive `Av(123)` when expanding 1x1 verified classes
- fix bug that prevented applying all eight symmetries
- fix assumption mapping bug in `FusionStrategy`
- fix `__repr__` in `FusionStrategy`

## [2.0.0] - 2020-06-17
### Added
All the necessary strategies for combinatorial exploration.

### Changed
Refactoring and speed up of many algorithm most notably the is empty check.

### Removed
- Support for Python 3.5 and earlier

## [1.0.2] - 2019-03-30
### Changed
- Update dependency versions

## [1.0.1] - 2019-08-26
### Changed
- Update comb_spec_searcher to 0.2.1

## [1.0.0] - 2019-08-26
### Added
- Remove factors from requirements if already implied by other requirement
list.
- Added tiling method `is_empty_cell` and `is_monotone_cell`
### Changed
- The `cell_basis` method of the tilings has an 1 obstruction for empty cell.
  The basis of a cell that is outside of the tiling is no longer defined.
- The requirement list in `cell_basis` method now finds intersections of
  requirement lists
- New `add_list_requirement` method to `Tiling`.
### Fixed
- Infinite recursion issue in get_genf.
- Close mongo when finished.

## [0.0.1] - 2019-06-02
### Added
- This changelog.

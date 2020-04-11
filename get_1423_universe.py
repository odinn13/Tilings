import gzip
import os
import pickle

from permuta import Perm
from tilings import Obstruction, Tiling
from tilings import strategies as strat
from tilings.tilescope import TileScope, TileScopePack

t_to_fuse = Tiling(
    obstructions=(
        Obstruction(Perm((2, 0, 1)), ((1, 0), (1, 0), (1, 0))),
        Obstruction(Perm((2, 0, 1)), ((1, 0), (1, 0), (2, 0))),
        Obstruction(Perm((2, 0, 1)), ((1, 0), (2, 0), (2, 0))),
        Obstruction(Perm((2, 0, 1)), ((2, 0), (2, 0), (2, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (0, 0), (0, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (0, 0), (1, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (0, 0), (2, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (1, 0), (1, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (1, 0), (2, 0))),
        Obstruction(Perm((0, 3, 1, 2)), ((0, 0), (0, 0), (2, 0), (2, 0))),
    ),
    requirements=(),
)


row_placements = strat.RowAndColumnPlacementStrategy(place_row=True, place_col=False)
fake_verification = strat.FakeVerificationStrategy([t_to_fuse])


pack = TileScopePack(
    initial_strats=[strat.FactorStrategy(), strat.RequirementPlacementStrategy(),],
    inferral_strats=[
        strat.RowColumnSeparationStrategy(),
        strat.ObstructionTransitivityStrategy(),
    ],
    expansion_strats=[[row_placements], [strat.AllCellInsertionStrategy()]],
    ver_strats=[
        strat.BasicVerificationStrategy(),
        strat.OneByOneVerificationStrategy(),
        strat.LocallyFactorableVerificationStrategy(),
        fake_verification,
    ],
    name="1423_pack",
)

css = TileScope("1423", pack)
max_depth = 10
for depth in range(1, max_depth + 1):
    css.do_level()
    if css.find_tree():
        print(f"Found a tree after depth {depth}")
        break
    universe_file = f"1423_universe_depth{depth}.pkl.gz"
    with gzip.open(universe_file, "w") as f:
        pickle.dump(css, f, protocol=4)
    print(css.status())

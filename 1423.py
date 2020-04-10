import itertools
from typing import List, Tuple

from permuta import Perm
from permuta.misc import DIR_EAST, DIR_NORTH, DIR_SOUTH
from tilings import GriddedPerm, Tiling
from tilings import strategies as strat
from tilings.tilescope import TileScope, TileScopePack


def print_name(name):
    print(">" * 20, name, "<" * 20)


def print_rule(rule):
    print(">>>>", rule)


strat_to_apply = []  # type: List[Tuple[Tiling, strat.abstract_strategy.Strategy]]
to_fake_verify = []  # type: List[Tiling]
row_placements = strat.RowAndColumnPlacementStrategy(place_row=True, place_col=False)


t0 = Tiling.from_string("1423")
print_name("F_0")
print(t0)

# Place row 0 south
t1 = t0.add_single_cell_obstruction(Perm((0,)), (0, 0))
(t2,) = t0.place_row(0, DIR_SOUTH)
strat_to_apply.append((t0, row_placements))
print_rule("F0 = F1 + F2")
print_name("F1")
print(t1)
print_rule("F1 = 1")
print_name("F2")
print(t2)

# Place row 1 south
t3 = t2.add_single_cell_obstruction(Perm((0,)), (2, 1)).add_single_cell_obstruction(
    Perm((0,)), (0, 1)
)
t4, t5 = t2.place_row(1, DIR_SOUTH)
strat_to_apply.append((t2, row_placements))
print_rule("F2 = F3 + F4 + F5")
print_name("F3")
print(t3)
print_rule("F3 = x")
print_name("F4")
print(t4)
print_name("F5")
print(t5)

t6, t7, _ = t4.find_factors()
assert t6.dimensions == (3, 1)
assert t7.dimensions == (1, 1)
strat_to_apply.append((t4, strat.FactorStrategy()))
print_rule("F4 = F6 * F7 * F7")
print_name("F6")
print(t6)
assert t6.fusion(col=1) in t2.find_factors()
to_fake_verify.append(t6)
print_rule("F6 = fuse to non trivial factor of F2")
print_name("F7")
print(t7)
print_rule("F7 = x")

t8 = t5.add_single_cell_obstruction(Perm((0,)), (2, 2))
t9 = t5.insert_cell((2, 2))
strat_to_apply.append((t5, strat.AllCellInsertionStrategy()))
print_rule("F5 = F8 + F9")
print_name("F8")
print(t8)
assert all(f in t8.find_factors() for f in t2.find_factors())
strat_to_apply.append((t8, strat.FactorStrategy(union=True)))
print_rule("F8 = F2 * F7")
print_name("F9")
print(t9)


t10 = t9.add_single_cell_obstruction(Perm((0,)), (4, 2))
t11 = t9.insert_cell((4, 2))
strat_to_apply.append((t9, strat.AllCellInsertionStrategy()))
print_rule("F9 = F10 + F11")
print_name("F10")
print(t10)
t10_1 = t10.place_point_in_cell((2, 2), DIR_NORTH)
strat_to_apply.append((t10, strat.RequirementPlacementStrategy()))
print(t10_1)
strat_to_apply.append((t10_1, strat.FactorStrategy(union=True)))
# to_fake_verify.append(t10_1)
print_name("F11")
print(t11)
t11_1 = t11.place_point_in_cell((4, 2), DIR_SOUTH)
strat_to_apply.append((t11, strat.RequirementPlacementStrategy()))
t11_2 = t11_1.place_point_in_cell((2, 2), DIR_NORTH)
strat_to_apply.append((t11_1, strat.RequirementPlacementStrategy()))
print(t11_2)


t12 = t11_2.add_single_cell_obstruction(Perm((0,)), (0, 4))
t13 = t11_2.insert_cell((0, 4))
strat_to_apply.append((t11_2, strat.AllCellInsertionStrategy()))
print_rule("F11 = F12 + F13")
print_name("F12")
print(t12)
t12_1 = t12.row_and_column_separation()
strat_to_apply.append((t12, strat.RowColumnSeparationStrategy()))
assert t12 != t12_1
print(t12_1)
strat_to_apply.append((t12_1, strat.FactorStrategy()))
to_fake_verify.extend(t12_1.find_factors())
print_name("F13")
print(t13)
t13_1 = t13.place_point_in_cell((0, 4), DIR_NORTH)
strat_to_apply.append((t13, strat.RequirementPlacementStrategy()))
t13_2 = t13_1.row_and_column_separation()
strat_to_apply.append((t13_1, strat.RowColumnSeparationStrategy()))
assert t13_1 != t13_2
print(t13_2)


t14 = t13_2.add_single_cell_obstruction(Perm((0,)), (3, 7))
t15 = t13_2.insert_cell((3, 7))
strat_to_apply.append((t13_2, strat.AllCellInsertionStrategy()))
print_rule("F13 = F14 + F15")


print_name("F14")
print(t14)
strat_to_apply.append((t14, strat.FactorStrategy()))
to_fake_verify.extend(t14.find_factors())
assert t14 == t14.row_and_column_separation()
print_name("F15")
print(t15)
t15_1 = t15.place_point_in_cell((3, 7), DIR_EAST)
strat_to_apply.append((t15, strat.RequirementPlacementStrategy()))
t15_2 = t15_1.row_and_column_separation()
strat_to_apply.append((t15_1, strat.RowColumnSeparationStrategy()))
assert t15_1 != t15_2
print(t15_2)
strat_to_apply.append((t15_2, strat.FactorStrategy()))
to_fake_verify.extend(t15_2.find_factors())

print("=" * 80)
print(" " * 30, "End of the main tree")
print("=" * 80)

build_universe = True
if build_universe:
    fake_verification = strat.FakeVerificationStrategy(to_fake_verify)
    pack = TileScopePack.point_placements()
    pack.expansion_strats.append([row_placements])
    pack.ver_strats.remove(strat.LocallyFactorableVerificationStrategy())
    pack = pack.add_verification(fake_verification)
    css = TileScope(t0, pack, debug=True)

    def apply_strat(tiling, strategy, inferral=False):
        label = css.classdb.get_label(tiling)
        try:
            css._expand_class_with_strategy(tiling, strategy, label)
        except TypeError:
            css._expand_class_with_strategy(tiling, strategy, label, inferral=True)

    for t, s in strat_to_apply:
        apply_strat(t, s)
    css.auto_search(max_time=0, smallest=True)

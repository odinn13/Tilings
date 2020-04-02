from permuta import Perm

better_bounds = {
    frozenset({Perm((0, 1)), Perm((1, 0))}): 1,
    frozenset({Perm((1, 0)), Perm((0, 1, 2))}): 1,
    frozenset({Perm((0, 1)), Perm((2, 1, 0))}): 1,
    frozenset({Perm((0, 1)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0)), Perm((0, 1, 2, 3))}): 1,
    frozenset({Perm((1, 0)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((0, 1)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1, 3)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1, 3)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2, 3)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 3, 2)), Perm((2, 3, 0, 1))}): 2,
    frozenset({Perm((1, 0, 2, 3)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2, 3)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((1, 2, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((1, 2, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 2, 0))}): 3,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 3, 2))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 3, 2))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((3, 2, 1, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 3))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 3, 2))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 3))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 2, 0, 1))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 3))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((3, 1, 2, 0))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 3))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 1, 3))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 3))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 2, 1, 3))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((2, 3, 0, 1))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 3, 2))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 1, 3))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 3, 2))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((2, 3, 0, 1))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 3))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 1, 2, 0))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 4, 3))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 4, 3))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 1, 4, 3))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 3, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 3, 1, 4))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 3, 2, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 3, 2, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 2, 1, 4))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 4, 3))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 2, 3, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 3, 2, 1, 4))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 2, 3, 0, 1))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 3, 2, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 3, 1, 2, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 1, 3, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 3, 2, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 3, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 1, 2, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((3, 4, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 4, 1, 2, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 3, 2, 4))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 1, 3, 4))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 2, 1, 4, 3))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 2, 1, 3, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 3, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 3, 1, 4))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 2, 3, 1, 4))}): 1,
    frozenset({Perm((3, 1, 2, 0)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((1, 0, 2, 3, 4))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 3, 2, 1, 4))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 3, 2, 1, 4))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((1, 0, 2, 3, 4))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 3, 1, 2, 4))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 1, 2, 4, 3))}): 1,
    frozenset({Perm((0, 2, 1, 3)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 2, 3, 1, 4))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 2, 1, 3, 4))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 1, 3, 2, 4))}): 1,
    frozenset({Perm((3, 2, 1, 0)), Perm((1, 0, 2, 4, 3))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 1, 2, 4, 3))}): 1,
    frozenset({Perm((1, 0, 2, 3)), Perm((3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2, 3)), Perm((3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 2, 1, 3, 4))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 1, 3, 2, 4))}): 1,
    frozenset({Perm((2, 3, 1, 0)), Perm((0, 3, 1, 2, 4))}): 1,
    frozenset({Perm((0, 1, 3, 2)), Perm((4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((3, 2, 0, 1)), Perm((0, 1, 2, 3, 4))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((2, 1, 0))}): 9,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 0, 1))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 0, 1))}): 6,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 2, 0)),
               Perm((2, 0, 1))}): 6,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((1, 2, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 2, 0)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((2, 0, 1)),
               Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 0, 1)), Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((1, 2, 0)),
               Perm((2, 0, 1)), Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((1, 2, 0)), Perm((2, 0, 1))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 2, 0)),
               Perm((2, 0, 1)), Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((1, 2, 0)), Perm((2, 1, 0))}): 6,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((1, 0, 2)),
               Perm((2, 0, 1)), Perm((2, 1, 0))}): 6,
    frozenset({Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((1, 0, 3, 2))}): 4,
    frozenset({Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((1, 0, 2, 3))}): 4,
    frozenset({Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((0, 2, 1, 3))}): 2,
    frozenset({Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((0, 1, 3, 2))}): 4,
    frozenset({Perm((1, 2, 0)), Perm((2, 0, 1)), Perm((0, 1, 2, 3))}): 4,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((3, 2, 0, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((3, 0, 1, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((3, 0, 2, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((0, 3, 1, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((0, 3, 2, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((0, 1, 3, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((1, 2, 0)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((1, 2, 0)), Perm((2, 1, 0)), Perm((1, 0, 3, 2))}): 3,
    frozenset({Perm((1, 2, 0)), Perm((2, 1, 0)), Perm((1, 0, 2, 3))}): 2,
    frozenset({Perm((1, 2, 0)), Perm((2, 1, 0)), Perm((0, 2, 1, 3))}): 2,
    frozenset({Perm((1, 2, 0)), Perm((2, 1, 0)), Perm((0, 1, 3, 2))}): 2,
    frozenset({Perm((1, 2, 0)), Perm((2, 1, 0)), Perm((0, 1, 2, 3))}): 2,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((3, 2, 0, 1))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((3, 0, 1, 2))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((2, 0, 1, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((1, 0, 2, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((3, 1, 0, 2))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((2, 1, 0, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 2, 0)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((3, 2, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((3, 0, 2, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((1, 0, 3, 2))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((3, 1, 0, 2))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((2, 1, 0, 3))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 2, 0)), Perm((0, 3, 2, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((1, 2, 3, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((2, 3, 1, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((1, 3, 2, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((0, 2, 3, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((0, 3, 2, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((0, 1, 3, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 0, 1)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((2, 0, 1)), Perm((2, 1, 0)), Perm((1, 0, 3, 2))}): 3,
    frozenset({Perm((2, 0, 1)), Perm((2, 1, 0)), Perm((1, 0, 2, 3))}): 2,
    frozenset({Perm((2, 0, 1)), Perm((2, 1, 0)), Perm((0, 2, 1, 3))}): 2,
    frozenset({Perm((2, 0, 1)), Perm((2, 1, 0)), Perm((0, 1, 3, 2))}): 2,
    frozenset({Perm((2, 0, 1)), Perm((2, 1, 0)), Perm((0, 1, 2, 3))}): 2,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((1, 2, 3, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((1, 2, 0, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((2, 3, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((1, 0, 2, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((2, 1, 3, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((2, 1, 0, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 0, 1)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((2, 3, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((1, 3, 2, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((1, 0, 3, 2))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((2, 1, 3, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((2, 1, 0, 3))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((3, 2, 1, 0))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 0, 1)), Perm((0, 3, 2, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((1, 2, 3, 0))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((3, 0, 1, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((2, 3, 0, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((0, 2, 3, 1))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((0, 3, 1, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((0, 1, 3, 2))}): 3,
    frozenset({Perm((1, 0, 2)), Perm((2, 1, 0)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((3, 2, 0, 1))}): 4,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((2, 3, 1, 0))}): 4,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((2, 3, 0, 1))}): 4,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((3, 2, 1, 0))}): 4,
    frozenset({Perm((0, 2, 1)), Perm((1, 0, 2)), Perm((3, 1, 2, 0))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((3, 2, 0, 1))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((2, 3, 1, 0))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((2, 3, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((3, 2, 1, 0))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((1, 0, 2)), Perm((3, 1, 2, 0))}): 2,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((1, 2, 3, 0))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((1, 2, 0, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((3, 0, 1, 2))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((2, 0, 1, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((1, 0, 2, 3))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((2, 3, 0, 1))}): 3,
    frozenset({Perm((0, 2, 1)), Perm((2, 1, 0)), Perm((0, 1, 2, 3))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 1, 0)), Perm((1, 3, 0, 2))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 1, 0)), Perm((2, 0, 3, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 1, 0)), Perm((1, 0, 3, 2))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((2, 1, 0)), Perm((2, 3, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((3, 2, 0, 1))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((2, 3, 1, 0))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((2, 3, 0, 1))}): 3,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((3, 2, 1, 0))}): 2,
    frozenset({Perm((0, 1, 2)), Perm((0, 2, 1)), Perm((3, 1, 2, 0))}): 2,
    frozenset({Perm((1, 0)), Perm((0, 1, 2, 3, 4, 5))}): 1,
    frozenset({Perm((0, 1)), Perm((5, 4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0)), Perm((0, 1, 2, 3, 4, 5, 6))}): 1,
    frozenset({Perm((0, 1)), Perm((6, 5, 4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 4, 2, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 3, 2, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 3, 2, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 4, 3, 2, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 4, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 3, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((1, 0, 2, 3, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 4, 1, 2, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 1, 2, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 1, 2, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 4, 1, 3, 2, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 2, 1, 3, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 2, 1, 3, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 4, 2, 1, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 2, 1, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 3, 2, 1, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 4, 2, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 3, 2, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 3, 2, 4, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 4, 3, 2, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 4, 3, 5))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 3, 5, 4))}): 1,
    frozenset({Perm((1, 2, 0)), Perm((0, 1, 2, 3, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 3, 4, 2, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 3, 2, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 3, 2, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 4, 3, 2, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 4, 3, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 3, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((1, 0, 2, 3, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 3, 4, 1, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 3, 1, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 3, 1, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 4, 3, 1, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 1, 3, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 2, 1, 3, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 3, 2, 4, 1, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 3, 2, 1, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 3, 2, 1, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 3, 4, 2, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 3, 2, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 3, 2, 4, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 4, 3, 2, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 4, 3, 5))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 3, 5, 4))}): 1,
    frozenset({Perm((2, 0, 1)), Perm((0, 1, 2, 3, 4, 5))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 2, 3, 4, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 2, 4, 3, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 3, 1, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 1, 2, 3, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 1, 3, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 2, 3, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 2, 3, 4, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 2, 4, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 3, 2, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 1, 3, 4, 2, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 1, 4, 2, 3, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((4, 5, 2, 3, 0, 1))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((1, 0, 2)), Perm((5, 1, 4, 3, 2, 0))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 4, 3, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 3, 5, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((1, 0, 2, 3, 4, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 3, 4, 1, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 4, 1, 3, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 3, 1, 4, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 3, 1, 4, 2, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 4, 1, 2, 3, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 3, 1, 2, 4, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 1, 3, 5, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 2, 1, 3, 4, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 3, 4, 1, 2, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 3, 4, 2, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 4, 2, 3, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 3, 2, 4, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 4, 3, 5))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 3, 5, 4))}): 1,
    frozenset({Perm((2, 1, 0)), Perm((0, 1, 2, 3, 4, 5))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 2, 3, 4, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 1, 2, 3, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 2, 4, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 2, 1, 3, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 2, 3, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 2, 3, 4, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 2, 3, 1, 4, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 1, 2, 3, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 1, 2, 4, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 2, 4, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 3, 2, 1, 4, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((4, 5, 2, 3, 0, 1))}): 1,
    frozenset({Perm((0, 2, 1)), Perm((5, 4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 3, 4, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 5, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 5, 3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 3, 1, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 2, 4, 1, 3, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 3, 4, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 3, 1, 4, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 2, 4, 3, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 1, 3, 2, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 2, 1, 4, 3, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 3, 2, 4, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 2, 1, 3, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 3, 2, 1, 4, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((4, 5, 3, 2, 0, 1))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 3, 2, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 4, 2, 3, 1, 0))}): 1,
    frozenset({Perm((0, 1, 2)), Perm((5, 1, 4, 3, 2, 0))}): 1,
}

import pytest

from solver import Solver


def test_no_root():
    assert Solver.solve(a=1, b=0, c=1) == []


def test_two_non_equal_roots():
    roots = Solver.solve(a=1, b=0, c=-1)
    assert len(roots) == 2
    assert roots[0] == -1 and roots[1] == 1


def test_two_equal_roots():
    roots = Solver.solve(a=1, b=2, c=1)
    assert len(roots) == 2
    assert roots[0] == roots[1] == -1


def test_too_small_a():
    with pytest.raises(ZeroDivisionError):
        Solver.solve(0, 2, 1)
        Solver.solve(-10e-7, 2, 1)


def test_too_small_D():
    assert Solver.solve(a=1, b=-2, c=1) == [1, 1]
    roots = Solver.solve(1.0, 2.000000001, 1.0)
    assert roots[0] == roots[1]


def incorrect_values():
    with pytest.raises(TypeError):
        Solver.solve("1", 2, 1)
        Solver.solve(b=2, c=1)
        Solver.solve(a=1, b={1: "test_value"}, c=-1)
        Solver.solve(a=1, b=0, c=[-1, 2])

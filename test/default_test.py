# import pytest

from solver import Solver

def test_no_root():
      assert Solver.solve(a=1, b=0, c=1) == None 

def test_two_equal_root():
      roots = Solver.solve(a=1, b=0, c=-1)
      assert len(roots) == 2
      assert roots[0] != roots[1]


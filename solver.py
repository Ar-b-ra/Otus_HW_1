from typing import Optional, List
from math import isclose, sqrt


class Solver:
    epsilon = 1e-9

    @classmethod
    def solve(cls, a: float, b: float, c: float) -> Optional[List[float]]:
        if not (isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (float, int))):
            raise TypeError("a, b, and c should be of type float or int")
        if isclose(a, 0, abs_tol=cls.epsilon):
            raise ZeroDivisionError("a should not be zero")

        D = b * b - 4 * a * c
        if D < 0:
            return []
        elif isclose(D, 0, abs_tol=cls.epsilon):
            D = 0

        return [
            (-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)
        ]


if __name__ == "__main__":
    print(Solver.solve(a=1, b=2, c=1))

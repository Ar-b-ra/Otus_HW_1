from math import sqrt
from typing import Optional


class Solver:
    epsilon = 10e-6

    @classmethod
    def solve(cls, a: float, b: float, c: float) -> Optional[list[float]]:
        if not any([isinstance(a, float), isinstance(a, int)]) and any(
                [isinstance(b, float), isinstance(b, int)]) and any([isinstance(c, float), isinstance(c, int)]):
            raise TypeError
        if abs(a) < cls.epsilon:
            raise ZeroDivisionError
        D = b * b - 4 * a * c
        if D < 0:
            return []
        elif D < cls.epsilon:
            D = 0
        return [
            (-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)
        ]


if __name__ == "__main__":
    print(Solver.solve(a=1, b=2, c=1))

from math import sqrt
from typing import Optional


class Solver:
    epsilon = 10e-6
    @classmethod
    def solve(cls, a: float, b: float, c: float) -> Optional[list[float]]:
        if abs(a) < cls.epsilon:
            raise ZeroDivisionError
        D = b*b - 4 * a * c
        if D < 0:
            return None
        elif D < cls.epsilon:
            D = 0
        return [
            (-b - sqrt(D))/(2*a), (-b + sqrt(D))/(2*a)
        ]


if __name__ == "__main__":
    print(Solver.solve(a=0, b=0, c=1))

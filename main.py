from math import sqrt
from typing import Optional


class Solver:
    @staticmethod
    def solve(a: float, b: float, c: float) -> Optional[list[float]]:
        if a == 0:
            raise ZeroDivisionError
        D = b*b - 4 * a * c
        if D < 0:
            return None
        return [
            (-b - sqrt(D))/(2*a), (-b + sqrt(D))/(2*a)
        ]


if __name__ == "__main__":
    print(Solver.solve(a=0, b=0, c=1))

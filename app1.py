"""
    Napisz program, w którym przechowasz informacje na temat punktu i przygotujesz funkcjonalność, dzięki
    której wyznaczysz odległość tego punktu od początku układu współrzędnych. Następnie z kolekcji punktów
    wyznacz ten, który znajduje się najdalej początku układu współrzędnych.
"""

import math
from dataclasses import dataclass

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

    def get_zero_distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def get_max_distance_point(points: list['Point']) -> 'Point':
        return max(points, key=lambda p: p.get_zero_distance())


def main() -> None:
    p1 = Point(10, 20)
    p2 = Point(30, 20)
    p3 = Point(10, 10)
    p4 = Point()
    points = [p1, p2, p3, p4]

    max_point = Point.get_max_distance_point(points)
    print(str(max_point))

if __name__ == '__main__':
    main()

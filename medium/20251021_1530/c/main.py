import math


class Point:
    def __init__(self, i: int, x: int, y: int):
        self.i = i
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


points: list[Point] = []

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    p = Point(i + 1, x, y)
    points.append(p)

for origin in points:
    current_top = 0
    answer = origin.i
    for destination in points:
        d = distance(origin, destination)
        if d > current_top:
            current_top = d
            answer = destination.i
    print(answer)

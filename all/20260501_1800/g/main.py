from itertools import combinations


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# points: list[Point] = []
points: set[Point] = set()
point_tuple_set: set[tuple[int, int]] = set()
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    point = Point(x, y)
    # points.append(point)
    points.add(point)
    point_tuple_set.add((x, y))

answer = 0
for v in combinations(points, 2):
    # print(v)
    p1 = v[0]
    p2 = v[1]
    if (
        p1.x != p2.x
        and p1.y != p2.y
        and (p1.x, p2.y) in point_tuple_set
        and (p2.x, p1.y) in point_tuple_set
    ):
        answer += 1

print(answer // 2)

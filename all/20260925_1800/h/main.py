from fractions import Fraction
from itertools import combinations


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return str((self.x, self.y))


# y軸に並行でない直線は、傾きa, 切片b、y_pararellはFalse、x_bは0
# y軸に並行な直線は、aに0、bに0、y_pararellはTrue、x_bにx切片
# ただし、y軸に並行な直線はaとbを0として、y_pararellx切片をおく
# y軸に並行でない直線は、y_pararellは0とする
class Line:
    def __init__(self, a: Fraction, b: Fraction, y_pararell: bool, x_b: int) -> None:
        self.a = a
        self.b = b
        self.y_pararell = y_pararell
        self.x_b = x_b

    def __eq__(self, other):
        if not isinstance(other, Line):
            raise
        return (
            self.a == other.a
            and self.b == other.b
            and self.y_pararell == other.y_pararell
            and self.x_b == other.x_b
        )

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.y_pararell, self.x_b))

    def __repr__(self) -> str:
        return str((self.a, self.b, self.y_pararell, self.x_b))


N, K = map(int, input().split())

if K == 1:
    print("Infinity")
    exit()

points: list[Point] = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append(Point(x, y))


# p1, p2を通る直線が通る点の集合
def through_points(p1: Point, p2: Point):
    result: set[Point] = set()
    if p1.x == p2.x:
        for p in points:
            if p.x == p1.x:
                result.add(p)
        return result
    if p1.y == p2.y:
        for p in points:
            if p.y == p1.y:
                result.add(p)
        return result
    for p in points:
        if (p.y - p1.y) * (p2.x - p1.x) == (p2.y - p1.y) * (p.x - p1.x):
            result.add(p)
    return result


def get_line(p1: Point, p2: Point):
    if p1.x == p2.x:
        return Line(Fraction(0, 1), Fraction(0, 1), True, p1.x)
    a = Fraction(p2.y - p1.y, p2.x - p1.x)
    b = -a * p1.x + p1.y
    return Line(a, b, False, 0)


answer_set: set[Line] = set()
for pair in combinations(points, 2):
    p1 = pair[0]
    p2 = pair[1]
    # print(pair, p1, p2)
    t_points = through_points(p1, p2)
    if len(t_points) >= K:
        answer_set.add(get_line(p1, p2))

# print(answer_set)
print(len(answer_set))

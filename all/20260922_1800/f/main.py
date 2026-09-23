N = int(input())
S = input()

points: set[tuple[int, int]] = set()
points.add((0, 0))


class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    @property
    def to_tuple(self):
        return (self.x, self.y)


point = Point()
for s in S:
    if s == "R":
        point.x += 1
    elif s == "L":
        point.x -= 1
    elif s == "U":
        point.y += 1
    elif s == "D":
        point.y -= 1

    t = point.to_tuple
    if t in points:
        print("Yes")
        exit()
    points.add(t)

print("No")

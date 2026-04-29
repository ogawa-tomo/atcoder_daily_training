# PyPyだとACだがCPythonだとTLE
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Circle:
    def __init__(self, x: int, y: int, r: int) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.size = 1
        self.parent: Circle | None = None

    @property
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root


def is_same(c1: Circle, c2: Circle):
    return c1.root == c2.root


def unite(c1: Circle, c2: Circle):
    root1 = c1.root
    root2 = c2.root
    if root1 == root2:
        raise
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


def distance2(sx: int, sy: int, tx: int, ty: int):
    return (sx - tx) ** 2 + (sy - ty) ** 2


def connected(c1: Circle, c2: Circle):
    d2 = distance2(c1.x, c1.y, c2.x, c2.y)
    # if d2 > (c1.r + c2.r)**2:
    #     # 離れている
    #     return False
    # if d2 < (c1.r - c2.r)**2:
    #     # 含んでいる
    #     return False
    # return True
    return (c1.r - c2.r) ** 2 <= d2 and d2 <= (c1.r + c2.r) ** 2


N = int(input())
sx, sy, tx, ty = map(int, input().split())

start_circle: Circle | None = None
goal_circle: Circle | None = None
circles: list[Circle] = []
for _ in range(N):
    x, y, r = map(int, input().split())
    circle = Circle(x, y, r)
    circles.append(circle)
    if distance2(sx, sy, circle.x, circle.y) == r**2:
        start_circle = circle
    if distance2(tx, ty, circle.x, circle.y) == r**2:
        goal_circle = circle

if start_circle is None or goal_circle is None:
    raise

for c1 in circles:
    for c2 in circles:
        if c1 == c2:
            continue
        if connected(c1, c2):
            if is_same(c1, c2):
                continue
            unite(c1, c2)

if is_same(start_circle, goal_circle):
    print("Yes")
else:
    print("No")

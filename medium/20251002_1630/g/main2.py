# WA
from collections import deque


class Grid:
    def __init__(self, empty: bool) -> None:
        self.empty = empty
        self.start = False
        self.goal = False
        self.medicine: int | None = None
        self.neighbors: list[Grid] = []
        # self.visited_with_medicine = False
        # self.visited_without_medicine = False
        # self.visited = False
        # self.highest_energy = -1
        self.energy = -1

    def __repr__(self):
        if self.start:
            return "S"
        elif self.goal:
            return "T"
        elif self.empty:
            return "."
        else:
            return "#"


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for h in range(H):
    data = list(input())
    row: list[Grid] = []
    for dd in data:
        if dd == "#":
            grid = Grid(False)
        else:
            grid = Grid(True)
        if dd == "S":
            grid.start = True
            start = grid
        elif dd == "T":
            grid.goal = True
        row.append(grid)
    grids.append(row)

# print(grids)
N = int(input())
for _ in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    grids[r][c].medicine = e

for h in range(H):
    for w in range(W):
        grid = grids[h][w]
        if not grid.empty:
            continue
        if h > 0:
            ue = grids[h - 1][w]
            if ue.empty:
                grid.neighbors.append(ue)
        if h < H - 1:
            shita = grids[h + 1][w]
            if shita.empty:
                grid.neighbors.append(shita)
        if w > 0:
            hidari = grids[h][w - 1]
            if hidari.empty:
                grid.neighbors.append(hidari)
        if w < W - 1:
            migi = grids[h][w + 1]
            if migi.empty:
                grid.neighbors.append(migi)

d: deque[Grid] = deque()

# このGridにこのエネルギーで到達したよ、とキューに保存するためのオブジェクトを用意する

# d.append(start)
# start.energy = 0
# while d:
#     grid = d.popleft()
#     energy = grid.energy
#     for neighbor in node.neighbors:
#         if neighbor.distance == -1:
#             d.append(neighbor)
#             neighbor.distance = distance + 1
# print("No")

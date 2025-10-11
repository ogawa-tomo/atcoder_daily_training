# AC
from collections import deque


class Grid:
    def __init__(self, empty: bool, h: int, w: int) -> None:
        self.h = h
        self.w = w
        self.empty = empty
        self.start = False
        self.goal = False
        self.medicine: int | None = None
        self.neighbors: list[Grid] = []
        self.neighbors_with_medicine: list[Grid] = []
        self.distance: int | None = None

    def __repr__(self):
        return f"{[self.h, self.w]}"


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for h in range(H):
    data = list(input())
    row: list[Grid] = []
    for w, dd in enumerate(data):
        if dd == "#":
            grid = Grid(False, h, w)
        else:
            grid = Grid(True, h, w)
        if dd == "S":
            grid.start = True
            start = grid
        elif dd == "T":
            grid.goal = True
            goal = grid
        row.append(grid)
    grids.append(row)

# print(grids)
N = int(input())
grids_with_medicine: list[Grid] = []
for _ in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    grid = grids[r][c]
    grid.medicine = e
    grids_with_medicine.append(grid)
if start not in grids_with_medicine:
    print("No")
    exit()
if goal not in grids_with_medicine:
    goal.medicine = 0
    grids_with_medicine.append(goal)


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


def reset_distance():
    for h in range(H):
        for w in range(W):
            grids[h][w].distance = None


# 薬のあるグリッド同士のネットワークを構築する
for start_grid in grids_with_medicine:
    if start_grid.medicine is None:
        raise
    reset_distance()
    d: deque[Grid] = deque()
    start_grid.distance = 0
    d.append(start_grid)
    while d:
        grid = d.popleft()
        distance = grid.distance
        if distance is None:
            raise
        if distance >= start_grid.medicine:
            continue
        for neighbor in grid.neighbors:
            if neighbor.distance is None:
                d.append(neighbor)
                neighbor.distance = distance + 1
                if neighbor.medicine is not None:
                    start_grid.neighbors_with_medicine.append(neighbor)

# 薬のあるグリッド同士のネットワークでスタートからゴールに行ければOK
for grid in grids_with_medicine:
    grid.distance = None
q: deque[Grid] = deque()
start.distance = 0
q.append(start)
while q:
    grid = q.popleft()
    distance = grid.distance
    if distance is None:
        raise
    for neighbor in grid.neighbors_with_medicine:
        if neighbor.distance is None:
            if neighbor.goal:
                print("Yes")
                exit()
            q.append(neighbor)
            neighbor.distance = distance + 1

print("No")

# WA
# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Grid:
    def __init__(self, empty: bool) -> None:
        self.empty = empty
        self.start = False
        self.goal = False
        self.medicine: int | None = None
        self.neighbors: list[Grid] = []
        self.visited_with_medicine = False
        self.visited_without_medicine = False
        self.visited = False
        self.highest_energy = -1

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
    for d in data:
        if d == "#":
            grid = Grid(False)
        else:
            grid = Grid(True)
        if d == "S":
            grid.start = True
            start = grid
        elif d == "T":
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

# print(start.neighbors)
# print(grids[3][3].goal)


# def dfs(grid: Grid, energy: int, use_medicine: bool):
#     if grid.goal:
#         print("Yes")
#         exit()
#     if use_medicine:
#         grid.visited_with_medicine = True
#     else:
#         grid.visited_without_medicine = True
#     if grid.medicine is not None and use_medicine:
#         energy = grid.medicine
#     energy -= 1
#     if energy < 0:
#         return
#     for neighbor in grid.neighbors:
#         if not neighbor.visited_with_medicine:
#             dfs(neighbor, energy, True)
#     for neighbor in grid.neighbors:
#         if not neighbor.visited_without_medicine:
#             dfs(neighbor, energy, False)


def dfs(grid: Grid, energy: int):
    if grid.goal:
        print("Yes")
        exit()
    grid.visited = True
    grid.highest_energy = max(grid.highest_energy, energy)
    if grid.medicine is not None and grid.medicine > energy:
        energy = grid.medicine
    energy -= 1
    if energy < 0:
        grid.visited = False
        return
    for neighbor in grid.neighbors:
        if not neighbor.visited and neighbor.highest_energy < energy:
            dfs(neighbor, energy)
    grid.visited = False


dfs(start, 0)
print("No")

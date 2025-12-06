# TLE
import copy

N = int(input())


class Grid:
    def __init__(self, black: bool):
        self.black = black

    def __repr__(self):
        if self.black:
            return "#"
        else:
            return "."


grids: list[list[Grid]] = []
for _ in range(N):
    A = list(input())
    row: list[Grid] = []
    for a in A:
        row.append(Grid(a == "#"))
    grids.append(row)

# print(grids)
# これだとO(N^3)なのでTLE
for i in range(N // 2):
    new_grids = copy.deepcopy(grids)
    for x in range(i, N - i):
        for y in range(i, N - i):
            new_grids[y][N - 1 - x].black = grids[x][y].black
    grids = new_grids

for i in range(N):
    print("".join([str(grid) for grid in grids[i]]))

import sys


class Grid:
    def __init__(self, state: str) -> None:
        self.state = state

    def is_black(self):
        return self.state == "#"

    def is_white(self):
        return self.state == "."

    def is_blank(self):
        return self.state == "?"

    def __repr__(self) -> str:
        return self.state


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for i in range(H):
    row: list[Grid] = []
    S = list(input())
    for s in S:
        row.append(Grid(s))
    grids.append(row)

# print(grids)
min_i = sys.maxsize
min_j = sys.maxsize
max_i = 0
max_j = 0

for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.is_black():
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        grid = grids[i][j]
        if grid.is_white():
            print("No")
            exit()

print("Yes")

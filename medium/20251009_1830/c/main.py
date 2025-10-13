class Grid:
    def __init__(self, i: int, j: int, empty: bool):
        self.i = i
        self.j = j
        self.empty = empty

    def __repr__(self):
        if self.empty:
            return "."
        else:
            return "#"


H, W = map(int, input().split())
Si, Sj = map(int, input().split())

grids: list[list[Grid]] = []
for h in range(H):
    row: list[Grid] = []
    C = list(input())
    for w in range(W):
        c = C[w]
        grid = Grid(h, w, c == ".")
        row.append(grid)
    grids.append(row)

X = list(input())
# print(grids)

# grid = grids[Si][Sj]
h = Si - 1
w = Sj - 1
for x in X:
    if x == "L" and w > 0 and grids[h][w - 1].empty:
        w -= 1
    elif x == "R" and w < W - 1 and grids[h][w + 1].empty:
        w += 1
    elif x == "U" and h > 0 and grids[h - 1][w].empty:
        h -= 1
    elif x == "D" and h < H - 1 and grids[h + 1][w].empty:
        h += 1

print(h + 1, w + 1)

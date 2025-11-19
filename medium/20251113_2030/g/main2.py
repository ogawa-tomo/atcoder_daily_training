# TLE
from itertools import combinations

print(3**12 * 2**8)


class Grid:
    def __init__(self, i: int, j: int, value: int):
        self.i = i
        self.j = j
        self.value = value
        self.set = False

    def __repr__(self):
        return str((self.i, self.j, self.value))


class Domino:
    def __init__(self, vertical: bool):
        self.vertical = vertical


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for i in range(H):
    row_data = list(map(int, input().split()))
    row: list[Grid] = []
    for j in range(W):
        v = row_data[j]
        grid = Grid(i, j, v)
        row.append(grid)
    grids.append(row)


def score():
    s = 0
    for i in range(H):
        for j in range(W):
            grid = grids[i][j]
            if not grid.set:
                s ^= grid.value
    return s


def reset():
    for i in range(H):
        for j in range(W):
            grid = grids[i][j]
            grid.set = False


for k in range(1 << H * W):
    # 各マスにドミノがあるかないか
    reset()
    for l in range(H * W):
        # この置き方が可能かどうかを判定したいのだが…簡単にできなそう
        if not (k >> l & 1):
            continue
        i = l // W
        j = l % W
        if grids[i][j].set:
            # 検討済みなら飛ばす
            continue
        # 右にドミノがあるか
        right_domino_exists = j < W - 1 and k >> (l + 1) & 1
        # 下にドミノがあるか
        below_domino_exists = i < H - 1 and k >> (l + W) & 1
        if right_domino_exists and below_domino_exists:
            two_right_domino_exists = j < W - 2 and k >> (l + 2) & 1
            two_below_domino_exists = i < H - 2 and k >> (l + 2 * W) & 1
            # if not

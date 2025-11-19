# TLE
from itertools import combinations


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


# print(grids)
answer = 0
for n in range(H * W // 2 + 1):
    # ドミノをn個置く場合 ←10通り
    for j in range(1 << n):
        dominos: list[Domino] = []
        # k個目のドミノが縦か横か ←2**10 = 1024通り
        for k in range(n):
            dominos.append(Domino(bool(j >> k & 1)))
        # n個のドミノをどこに置くか 20C10 =184756通り ここに無駄がありそう
        for pattern in combinations(list(range(H * W)), n):
            # print(pattern)
            # グリッドをリセット
            reset()
            succeeded = True  # このパターンで置けたか
            for l, p in enumerate(pattern):
                domino = dominos[l]
                # このドミノを置く座標
                i = p // W
                j = p % W
                grid = grids[i][j]
                if domino.vertical:
                    if i == H - 1:
                        succeeded = False
                        break
                    below_grid = grids[i + 1][j]
                    if grid.set or below_grid.set:
                        succeeded = False
                        break
                    grid.set = True
                    below_grid.set = True
                else:
                    if j == W - 1:
                        succeeded = False
                        break
                    right_grid = grids[i][j + 1]
                    if grid.set or right_grid.set:
                        succeeded = False
                        break
                    grid.set = True
                    right_grid.set = True
            if not succeeded:
                continue
            answer = max(answer, score())

print(answer)

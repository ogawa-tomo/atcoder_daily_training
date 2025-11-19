class Grid:
    def __init__(self, i: int, j: int, value: int):
        self.i = i
        self.j = j
        self.value = value

    def __repr__(self):
        return str((self.i, self.j, self.value))


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


# 可能なドミノの置き方のビット列
# ビット列のパターンは2^HW通りで、HWマスについて調べていくので計算量はO(HW*2^HW)になる
possible_dominos = [0]
for i in range(H):
    for j in range(W):
        # このマスのbit
        bit = i * W + j
        # このマスに横向きにドミノを置くビット列
        horizontal_domino = 3 << bit
        # このマスに縦向きにドミノを置くビット列
        vertical_domino = ((1 << W) + 1) << bit
        additional_dominos: list[int] = []
        for possible_domino in possible_dominos:
            # 横向きに置ければ、可能な置き方にそのパターンを追加
            if j < W - 1 and not (possible_domino & horizontal_domino):
                additional_dominos.append(possible_domino | horizontal_domino)
            # 縦向きに置ければ、可能な置き方にそのパターンを追加
            if i < H - 1 and not (possible_domino & vertical_domino):
                additional_dominos.append(possible_domino | vertical_domino)
        possible_dominos.extend(additional_dominos)

answer = 0
for possible_domino in possible_dominos:
    score = 0
    for i in range(H):
        for j in range(W):
            bit = i * W + j
            if (~possible_domino >> bit) & 1:
                score ^= grids[i][j].value
    answer = max(answer, score)

print(answer)

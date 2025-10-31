N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

P -= 1
Q -= 1
R -= 1
S -= 1

grids: list[list[str]] = []
for i in range(Q - P + 1):
    row: list[str] = []
    for j in range(S - R + 1):
        # 絶対座標
        ii = P + i
        jj = R + j

        # A, Bから見た相対位置
        di = ii - (A - 1)
        dj = jj - (B - 1)

        # print(i, j)
        # print(di, dj)
        if di == dj:
            if max(1 - A, 1 - B) <= di and di <= min(N - A, N - B):
                row.append("#")
                continue

        if di == -dj:
            if max(1 - A, B - N) <= di and di <= min(N - A, B - 1):
                row.append("#")
                continue

        row.append(".")
    grids.append(row)

for row in grids:
    print("".join(row))

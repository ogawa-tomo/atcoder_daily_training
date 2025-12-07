N = 9
grids: list[list[int]] = []
for _ in range(N):
    row = list(map(int, input().split()))
    grids.append(row)

# print(grids)

# 行
for i in range(N):
    emerged: set[int] = set()
    for j in range(N):
        num = grids[i][j]
        if num in emerged:
            print("No")
            exit()
        emerged.add(num)

# 列
for j in range(N):
    emerged = set()
    for i in range(N):
        num = grids[i][j]
        if num in emerged:
            print("No")
            exit()
        emerged.add(num)

# グリッド
for i in range(3):
    for j in range(3):
        start_i = 3 * i
        start_j = 3 * j
        emerged = set()
        for ii in range(start_i, start_i + 3):
            for jj in range(start_j, start_j + 3):
                num = grids[ii][jj]
                if num in emerged:
                    print("No")
                    exit()
                emerged.add(num)


print("Yes")

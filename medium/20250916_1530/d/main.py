N, M = map(int, input().split())

grids: list[list[str]] = []
for _ in range(N):
    row = list(input())
    grids.append(row)

# print(grids)
answers: list[list[int]] = []
for i in range(N - 8):
    for j in range(M - 8):
        is_tak_code = True
        # 左上
        for ii in range(i, i + 3):
            for jj in range(j, j + 3):
                if grids[ii][jj] == ".":
                    is_tak_code = False
                    break
        # 右下
        for ii in range(i + 6, i + 9):
            for jj in range(j + 6, j + 9):
                if grids[ii][jj] == ".":
                    is_tak_code = False
                    break

        # 左上
        for ii in range(i, i + 4):
            if grids[ii][j + 3] == "#":
                is_tak_code = False
                break
        for jj in range(j, j + 4):
            if grids[i + 3][jj] == "#":
                is_tak_code = False
                break
        # 右下
        for ii in range(i + 5, i + 9):
            if grids[ii][j + 5] == "#":
                is_tak_code = False
        for jj in range(j + 5, j + 9):
            if grids[i + 5][jj] == "#":
                is_tak_code = False
                break
        if is_tak_code:
            answers.append([i, j])

for answer in answers:
    print(" ".join(str(a + 1) for a in answer))

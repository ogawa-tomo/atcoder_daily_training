N, M = map(int, input().split())
S: list[list[str]] = []
T: list[list[str]] = []

for i in range(N):
    row = list(input())
    S.append(row)
for i in range(M):
    row = list(input())
    T.append(row)

# print(S)
# print(T)
for i in range(N - M + 1):
    for j in range(N - M + 1):
        matched = True
        # print(i, j)
        for ii in range(M):
            for jj in range(M):
                if S[i + ii][j + jj] != T[ii][jj]:
                    matched = False
                    break
            if not matched:
                break
        if matched:
            print(i + 1, j + 1)
            exit()

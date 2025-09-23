N, M = map(int, input().split())

S: list[list[str]] = []
T: list[list[str]] = []

for _ in range(N):
    row = list(input())
    S.append(row)
for _ in range(M):
    row = list(input())
    T.append(row)

for i in range(N - M + 1):
    for j in range(N - M + 1):
        equal = True
        for ii in range(M):
            for jj in range(M):
                if S[i + ii][j + jj] != T[ii][jj]:
                    equal = False
                    break
            if not equal:
                break
        if equal:
            print(i + 1, j + 1)
            exit()

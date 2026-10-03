from collections import defaultdict


N, T = map(int, input().split())
A = list(map(int, input().split()))

# row[i]: i行目の穴が空いた数
row: defaultdict[int, int] = defaultdict(int)
# column [i]: i行目の穴が空いた数
column: defaultdict[int, int] = defaultdict(int)
diagonal1 = 0
diagonal2 = 0

for t in range(T):
    a = A[t] - 1

    i = a // N
    row[i] += 1
    if row[i] == N:
        print(t + 1)
        exit()

    j = a % N
    column[j] += 1
    if column[j] == N:
        print(t + 1)
        exit()

    if i == j:
        diagonal1 += 1
        if diagonal1 == N:
            print(t + 1)
            exit()

    if i + j == N - 1:
        diagonal2 += 1
        if diagonal2 == N:
            print(t + 1)
            exit()

print(-1)

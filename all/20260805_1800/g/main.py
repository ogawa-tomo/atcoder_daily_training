import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp: list[list[int]] = []
for i in range(M + 1):
    before_max_a = -sys.maxsize
    row: list[int] = []
    for j in range(N):
        a = A[j]
        if i == 0:
            row.append(0)
            continue
        if j < i - 1:
            row.append(-sys.maxsize)
            continue
        before_max_a = max(dp[i - 1][j - 1], before_max_a)
        row.append(before_max_a + a * i)
    dp.append(row)

# for r in dp:
#     print(r)

print(max(dp[M]))

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][k][d]: 最初のi個の中からk個を選んで作れるd余る数の最大値
dp: list[list[list[int]]] = []
for _ in range(N + 1):
    dp_k: list[list[int]] = []
    for _ in range(N + 1):
        dp_k.append([-1] * D)
    dp.append(dp_k)

# print(dp)
dp[0][0][0] = 0

for i in range(N):
    for j in range(N):
        for d in range(D):
            if dp[i][j][d] == -1:
                continue

            # 選ばない場合
            dp[i + 1][j][d] = max(dp[i + 1][j][d], dp[i][j][d])

            # 選ぶ場合
            dp[i + 1][j + 1][(d + A[i]) % D] = max(
                dp[i + 1][j + 1][(d + A[i]) % D], dp[i][j][d] + A[i]
            )

print(dp[N][K][0])

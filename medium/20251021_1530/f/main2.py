N, M, K = map(int, input().split())
mod = 998244353

# dp[i][j]: 先頭からi項まで決めたときに、和がjである並べ方の数
# 0<=i<=N, 0<=j<=K
dp: list[list[int]] = []

for _ in range(N + 1):
    dp.append([0] * (K + 1))
dp[0][0] = 1
# print(dp)
for i in range(1, N + 1):
    # i項まで決めたとき
    for j in range(1, K + 1):
        # 和がjになる
        for m in range(1, M + 1):
            # 出た目がmだったときの場合の数
            if j - m >= 0:
                dp[i][j] += dp[i - 1][j - m]
                dp[i][j] %= mod
# print(dp)
print(sum(dp[N]) % mod)

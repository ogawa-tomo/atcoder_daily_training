N, X, Y = map(int, input().split())

# dp[n]["red"]: レベルnの赤の数
# dp[n]["blue"]: レベルnの青の数
dp: list[dict[str, int]] = []
for _ in range(N + 1):
    dp.append({"red": 0, "blue": 0})

dp[N]["red"] = 1
for n in range(N, 1, -1):
    # レベルnの赤を、n-1の赤と、nの青X個に変える
    dp[n - 1]["red"] += dp[n]["red"]
    dp[n]["blue"] += dp[n]["red"] * X
    dp[n]["red"] = 0

    # レベルnの青を、n-1の赤と、n-1の青Y個に変える
    dp[n - 1]["red"] += dp[n]["blue"]
    dp[n - 1]["blue"] += dp[n]["blue"] * Y
    dp[n]["blue"] = 0

print(dp[1]["blue"])

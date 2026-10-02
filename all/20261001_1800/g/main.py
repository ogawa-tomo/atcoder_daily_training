N = int(input())
A = list(map(int, input().split()))

# dp["odd"][i]: i番目のモンスターを処理したとき奇数体のモンスターを倒した状態として、そのときの最大値
dp: dict[str, list[int]] = {}
dp["odd"] = [0] * N
dp["even"] = [0] * N
dp["odd"][0] = A[0]

for i in range(1, N):
    dp["odd"][i] = max(dp["odd"][i - 1], dp["even"][i - 1] + A[i])
    dp["even"][i] = max(dp["even"][i - 1], dp["odd"][i - 1] + A[i] * 2)

# print(dp)
print(max(dp["odd"][N - 1], dp["even"][N - 1]))

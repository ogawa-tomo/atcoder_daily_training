# AC
import sys


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_taken_times: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_taken_times.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_taken_times[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N, K, T = map(int, input().split())
P = list(map(int, input().split()))

cum_sum = CumulativeSum(P)

# dp[t][k]: 時刻tまでにk回乗り終わっているとき、濡れる量の最小値
dp: list[list[int]] = []
dp.append([sys.maxsize] * (K + 1))
dp[0][0] = 0
for t in range(1, N + 1):
    dp_t: list[int] = []
    for k in range(K + 1):
        wet = dp[t - 1][k]
        if t - T >= 0 and k >= 1:
            # この時刻に乗り終わるように乗ったときの濡れる量
            wet = min(wet, dp[t - T][k - 1] + cum_sum.range_sum(t - T, t - 1))
        dp_t.append(wet)
    dp.append(dp_t)

print(dp[N][K])

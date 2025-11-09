# TLE & WA
import sys

sys.setrecursionlimit(10**9)


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


class Take:
    def __init__(self, start_time: int):
        self.start_time = start_time
        self.end_time = self.start_time + T - 1
        self.wet = cum_sum.range_sum(self.start_time, self.end_time)

    def __lt__(self, other):
        return self.wet < other.wet

    def __repr__(self):
        return str([self.start_time, self.end_time, self.wet])


takes: list[Take] = []
for t in range(N - T + 1):
    # print(t)
    takes.append(Take(t))


# 現在のテイク数と、現在の濡れと、次に乗れる時刻を与えたとき、濡れの量の最小値
def min_wet(current_takes_num: int, current_wet: int, next_time: int):
    if current_takes_num == K:
        return current_wet
    remaining_takes_num = K - current_takes_num
    # 不可能なら、最大値を返す
    if next_time >= N - remaining_takes_num * T:
        return sys.maxsize
    # 次回以降のテイクの最小値を返す
    result = sys.maxsize
    for t in range(next_time, N - remaining_takes_num * T):
        next_take = takes[t]
        wet = min_wet(
            current_takes_num + 1, current_wet + next_take.wet, next_take.end_time + 1
        )
        result = min(wet, result)
    return result


print(min_wet(0, 0, 0))

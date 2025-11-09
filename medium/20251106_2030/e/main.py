# TLE & WA
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

# print(takes)
takes.sort()

# 区間ごとの、既に乗っている数
taken_times = [0] * N


def can_take(take: Take):
    for time in range(take.start_time, take.end_time + 1):
        if taken_times[time] > 0:
            return False
    return True


best_takes: list[Take] = []
while len(best_takes) < K:
    for take in takes:
        if not can_take(take):
            continue
        best_takes.append(take)
        for t in range(take.start_time, take.end_time + 1):
            taken_times[t] += 1
        if len(best_takes) == K:
            break
# print(best_takes)
# print(taken_times)
answer = 0
for take in best_takes:
    answer += take.wet
print(answer)

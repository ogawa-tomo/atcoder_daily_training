import math


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N = int(input())
A = list(map(int, input().split()))

A.sort()
maxA = max(A)

# C[x]: Ai = x となるiの数
C = [0] * (10**6 + 1)
# C = [0] * 20
for a in A:
    C[a] += 1

cum_sum = CumulativeSum(C)
# print(C)


# Aj // d == n を満たすjの数
# ただし、Aj == d となるjは除外
def f(d: int, n: int):
    if n == 1:
        left = d + 1  # Aj == dは除外
    else:
        left = d * n
    right = min(d * (n + 1) - 1, 10**6)
    if left > right:
        return 0
    # print(left, right)
    return cum_sum.range_sum(left, right)


distinct_A = list(set(A))
answer = 0
for a in distinct_A:
    for n in range(1, maxA // a + 1):
        answer += n * f(a, n) * C[a]

# 重複した数字の組み合わせ
for a in distinct_A:
    answer += math.comb(C[a], 2)


print(answer)

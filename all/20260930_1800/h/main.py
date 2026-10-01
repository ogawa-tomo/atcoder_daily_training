# WA
N, M = map(int, input().split())
A = list(map(int, input().split()))


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


# A.sort()
# for i in range(N):
#     A[i] %= M
A = [a % M for a in A]
print(A)
cum_sum = CumulativeSum(A)
new_list = [n % M for n in cum_sum.cumulative_sum_list]
# cum_sum2 = CumulativeSum(cum_sum.cumulative_sum_list)
cum_sum2 = CumulativeSum(new_list)
print(cum_sum.cumulative_sum_list)
print(cum_sum2.cumulative_sum_list)
total = 0
for i in range(N):
    if i == 0:
        geta = 0
    else:
        geta = cum_sum.range_sum(0, i - 1)
    row_sum = cum_sum2.range_sum(i, N - 1) - geta * (N - i)
    # 足すとMを超える要素の数を求める
    # ok: Mを超えるインデックス
    ok = N
    ng = i - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if new_list[mid] - geta >= M:
            ok = mid
        else:
            ng = mid
    num = N - ok
    print(row_sum, geta, num)

    # total += row_sum - M * num
    total += row_sum


print(total)

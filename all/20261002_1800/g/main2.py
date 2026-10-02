# AC
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
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cum_sum_A = CumulativeSum(A)
cum_sum_B = CumulativeSum(B)
cum_sum_C = CumulativeSum(C)


class BCSplit:
    def __init__(self, j: int) -> None:
        self.j = j
        self.total = cum_sum_B.range_sum(0, j) + cum_sum_C.range_sum(j + 1, N - 1)

    def __lt__(self, other):
        if not isinstance(other, BCSplit):
            raise
        return self.total < other.total


bc_splits: list[BCSplit] = []
for j in range(1, N - 1):
    bc_split = BCSplit(j)
    bc_splits.append(bc_split)

bc_splits.sort()


answer = 0
for i in range(N - 2):
    a_sum = cum_sum_A.range_sum(0, i)
    while bc_splits[-1].j <= i:
        bc_splits.pop()
    bc_split = bc_splits[-1]
    bc_sum = bc_split.total - cum_sum_B.range_sum(0, i)
    abc_sum = a_sum + bc_sum
    answer = max(answer, abc_sum)
print(answer)

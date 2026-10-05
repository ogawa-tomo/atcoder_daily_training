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

cum_sum = CumulativeSum(A)
answer = 0
for i in range(1, N):
    answer += A[i] * cum_sum.range_sum(0, i - 1)
print(answer)

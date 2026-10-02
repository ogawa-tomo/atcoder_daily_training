# WA
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

answer = 0
j = 0
for i in range(N - 2):
    a_sum = cum_sum_A.range_sum(0, i)
    if j <= i:
        j = i + 1
    while True:
        b_sum = cum_sum_B.range_sum(i + 1, j)
        c_sum = cum_sum_C.range_sum(j + 1, N - 1)
        all_sum = a_sum + b_sum + c_sum
        answer = max(answer, all_sum)

        if j >= N - 2:
            break

        # jを伸ばして増えなくなった点が最適、とは限らない
        new_b_sum = cum_sum_B.range_sum(i + 1, j + 1)
        new_c_sum = cum_sum_C.range_sum(j + 2, N - 1)
        new_all_sum = a_sum + new_b_sum + new_c_sum
        if new_all_sum >= all_sum:
            j += 1
        else:
            break

print(answer)

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


N, L, R = map(int, input().split())
S = input()

# cumulative_sums[s]: 文字sの累積和
cumulative_sums: dict[str, CumulativeSum] = {}

alphabets = "abcdefghijklmnopqrstuvwxyz"
for alphabet in alphabets:
    array: list[int] = []
    for s in S:
        if s == alphabet:
            array.append(1)
        else:
            array.append(0)
    cumulative_sum = CumulativeSum(array)
    cumulative_sums[alphabet] = cumulative_sum

answer = 0
for i, s in enumerate(S):
    if i + L > N - 1:
        continue
    n = cumulative_sums[s].range_sum(i + L, min(i + R, N - 1))
    answer += n

print(answer)

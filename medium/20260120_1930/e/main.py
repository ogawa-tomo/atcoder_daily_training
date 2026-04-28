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
S: list[list[int]] = []
for _ in range(N):
    row_data = list(input())
    s: list[int] = []
    for d in row_data:
        if d == "#":
            s.append(1)
        else:
            s.append(0)
    S.append(s)

# print(S)


def is_ok(row: list[int]):
    if len(row) < 6:
        return False
    cum_sum = CumulativeSum(row)
    for j in range(len(row) - 5):
        if cum_sum.range_sum(j, j + 5) >= 4:
            return True
    return False


# 行
for i in range(N):
    row = S[i]
    if is_ok(row):
        print("Yes")
        exit()
# 列
for i in range(N):
    column: list[int] = []
    for j in range(N):
        column.append(S[j][i])
    if is_ok(column):
        print("Yes")
        exit()

# 斜め
for i in range(N):
    # (i, 0)...(0, i)
    row: list[int] = []
    for j in range(i + 1):
        row.append(S[i - j][j])
    if is_ok(row):
        print("Yes")
        exit()

    # (i, 0)...(N-1, N-1-i)
    row: list[int] = []
    for j in range(N - i):
        row.append(S[i + j][j])
    if is_ok(row):
        print("Yes")
        exit()

    # (N-1, i)...(i, N-1)
    row: list[int] = []
    for j in range(i, N):
        row.append(S[N - 1 - j + i][j])
    if is_ok(row):
        print("Yes")
        exit()

    # (0, i)...(N-1-i, N-1)
    row: list[int] = []
    for j in range(N - i):
        row.append(S[j][i + j])
    if is_ok(row):
        print("Yes")
        exit()

print("No")

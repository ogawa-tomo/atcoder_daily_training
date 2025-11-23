# TLE/WA
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


N, Q = map(int, input().split())


grid_pattern: list[list[str]] = []
row_cumulative_sums: list[CumulativeSum] = []
for _ in range(N):
    row_ = list(input())
    grid_pattern.append(row_)
    row_int: list[int] = []
    for r in row_:
        if r == "B":
            row_int.append(1)
        else:
            row_int.append(0)
    cum_sum = CumulativeSum(row_int)
    row_cumulative_sums.append(cum_sum)


# row行目において、startからendまでの黒の数
def blacks_row(row: int, start_column: int, end_column: int):
    row_mod = row % N
    return row_cumulative_sums[row_mod].range_sum(start_column % N, end_column % N)


for _ in range(Q):
    start_row, start_column, end_row, end_column = map(int, input().split())
    repeat_start_column = (
        start_column + (N - (start_column % N))
        if start_column % N != 0
        else start_column
    )
    repeat_end_column = (
        end_column - (end_column % N) - 1 if end_column % N != N - 1 else end_column
    )
    repeat_start_row = (
        start_row + (N - (start_row % N)) if start_row % N != 0 else start_row
    )
    repeat_end_row = end_row - (end_row % N) - 1 if end_row % N != N - 1 else end_row
    # print("column", repeat_start_column, repeat_end_column)
    # print("row", repeat_start_row, repeat_end_row)

    if repeat_end_column < repeat_start_column:
        column_repetition = 0
    else:
        column_repetition = (repeat_end_column + 1 - repeat_start_column) // N
    if repeat_end_row < repeat_start_row:
        row_repetition = 0
    else:
        row_repetition = (repeat_end_row + 1 - repeat_start_row) // N

    # column_repetition = (repeat_end_column - repeat_start_column)
    # row_repetition = (end_row // N) - (start_row // N) - 1
    # print("repetition", column_repetition, row_repetition)

    answer = 0
    for row in range(start_row, repeat_start_row):
        if start_column < repeat_start_column:
            answer += blacks_row(row, start_column, repeat_start_column - 1)
        answer += blacks_row(row, 0, N - 1) * column_repetition
        if repeat_end_column < end_column:
            answer += blacks_row(row, repeat_end_column + 1, end_column)

    repeat_part = 0
    for row in range(N):
        if start_column < repeat_start_column:
            repeat_part += blacks_row(row, start_column, repeat_start_column - 1)
        repeat_part += blacks_row(row, 0, N - 1) * column_repetition
        if repeat_end_column < end_column:
            repeat_part += blacks_row(row, repeat_end_column + 1, end_column)
    answer += repeat_part * row_repetition

    for row in range(repeat_end_row + 1, end_row + 1):
        if start_column < repeat_start_column:
            answer += blacks_row(row, start_column, repeat_start_column - 1)
        answer += blacks_row(row, 0, N - 1) * column_repetition
        if repeat_end_column < end_column:
            answer += blacks_row(row, repeat_end_column + 1, end_column)

    print(answer)

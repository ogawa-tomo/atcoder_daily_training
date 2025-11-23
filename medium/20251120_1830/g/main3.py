# AC
class CumulativeSum2D:
    def __init__(self, grids: list[list[int]]):
        self.grids = grids
        self.cum_sum_grids: list[list[int]] = []
        for i in range(len(grids)):
            row_cum_sum: list[int] = []
            total = 0
            for j in range(len(grids[i])):
                total += grids[i][j]
                row_cum_sum.append(total)
            self.cum_sum_grids.append(row_cum_sum)
        for i in range(len(grids)):
            if i == 0:
                continue
            for j in range(len(grids[i])):
                self.cum_sum_grids[i][j] += self.cum_sum_grids[i - 1][j]

    def range_sum(self, min_i, min_j, max_i, max_j):
        if min_i == 0 and min_j == 0:
            return self.cum_sum_grids[max_i][max_j]
        elif min_i == 0 and min_j > 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[max_i][min_j - 1]
            )
        elif min_i > 0 and min_j == 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[min_i - 1][max_j]
            )
        else:
            return (
                self.cum_sum_grids[max_i][max_j]
                - self.cum_sum_grids[max_i][min_j - 1]
                - self.cum_sum_grids[min_i - 1][max_j]
                + self.cum_sum_grids[min_i - 1][min_j - 1]
            )


N, Q = map(int, input().split())
grids: list[list[int]] = []

for _ in range(N):
    row_data = list(input())
    row: list[int] = []
    for d in row_data:
        if d == "B":
            row.append(1)
        else:
            row.append(0)
    grids.append(row)

# print(grids)
cum_sum_2d = CumulativeSum2D(grids)

for _ in range(Q):
    min_i, min_j, max_i, max_j = map(int, input().split())
    min_i_r = min_i % N
    min_j_r = min_j % N
    max_i_r = max_i % N
    max_j_r = max_j % N
    repeat_start_i = min_i if min_i_r == 0 else min_i + N - min_i_r
    repeat_end_i = max_i if max_i_r == N - 1 else max_i - max_i_r - 1
    repeat_start_j = min_j if min_j_r == 0 else min_j + N - min_j_r
    repeat_end_j = max_j if max_j_r == N - 1 else max_j - max_j_r - 1
    i_repetition = (
        (repeat_end_i - repeat_start_i + 1) // N if repeat_start_i < repeat_end_i else 0
    )
    j_repetition = (
        (repeat_end_j - repeat_start_j + 1) // N if repeat_start_j < repeat_end_j else 0
    )
    i_over = max_i // N > min_i // N
    j_over = max_j // N > min_j // N

    answer = 0
    if not i_over:
        # iの繰り返しがないとき
        if not j_over:
            answer += cum_sum_2d.range_sum(min_i_r, min_j_r, max_i_r, max_j_r)
        else:
            # 左
            if min_j_r > 0:
                answer += cum_sum_2d.range_sum(min_i_r, min_j_r, max_i_r, N - 1)
            # 中
            answer += cum_sum_2d.range_sum(min_i_r, 0, max_i_r, N - 1) * j_repetition
            # 右
            if max_j_r < N - 1:
                answer += cum_sum_2d.range_sum(min_i_r, 0, max_i_r, max_j_r)
    else:
        # iの繰り返しがあるとき

        if not j_over:

            # 上

            if min_i_r > 0:
                answer += cum_sum_2d.range_sum(min_i_r, min_j_r, N - 1, max_j_r)

            # 中
            answer += cum_sum_2d.range_sum(0, min_j_r, N - 1, max_j_r) * i_repetition

            # 下
            if max_i_r < N - 1:
                answer += cum_sum_2d.range_sum(0, min_j_r, max_i_r, max_j_r)
        else:
            if min_i_r > 0:
                if min_j_r > 0:
                    # 左上
                    answer += cum_sum_2d.range_sum(min_i_r, min_j_r, N - 1, N - 1)
                # 上
                answer += cum_sum_2d.range_sum(min_i_r, 0, N - 1, N - 1) * j_repetition
                if max_j_r < N - 1:
                    # 右上
                    answer += cum_sum_2d.range_sum(min_i_r, 0, N - 1, max_j_r)
            if max_i_r < N - 1:
                if min_j_r > 0:
                    # 左下
                    answer += cum_sum_2d.range_sum(0, min_j_r, max_i_r, N - 1)
                # 下
                answer += cum_sum_2d.range_sum(0, 0, max_i_r, N - 1) * j_repetition
                if max_j_r < N - 1:
                    # 右下
                    answer += cum_sum_2d.range_sum(0, 0, max_i_r, max_j_r)
            if min_j_r > 0:
                # 左
                answer += cum_sum_2d.range_sum(0, min_j_r, N - 1, N - 1) * i_repetition
            # 中
            answer += (
                cum_sum_2d.range_sum(0, 0, N - 1, N - 1) * i_repetition * j_repetition
            )
            if max_j_r < N - 1:
                # 右
                answer += cum_sum_2d.range_sum(0, 0, N - 1, max_j_r) * i_repetition
    print(answer)

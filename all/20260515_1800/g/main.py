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
        # print(self.cum_sum_grids)

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
    row_input = list(input())
    row: list[int] = []
    for r in row_input:
        if r == "B":
            row.append(1)
        else:
            row.append(0)
    grids.append(row)

cum_sum_2d = CumulativeSum2D(grids)
for _ in range(Q):
    a, b, c, d = map(int, input().split())

    # 縦方向の繰り返しパターン
    q_a = a // N
    q_c = c // N
    q_b = b // N
    q_d = d // N
    r_a = a % N
    r_c = c % N
    r_b = b % N
    r_d = d % N

    answer = 0
    if q_a == q_c and q_b == q_d:
        answer += cum_sum_2d.range_sum(r_a, r_b, r_c, r_d)
    # 横だけ繰り返しあり
    elif q_a == q_c and q_b != q_d:
        # 左
        answer += cum_sum_2d.range_sum(r_a, r_b, r_c, N - 1)
        # 繰り返し
        answer += cum_sum_2d.range_sum(r_a, 0, r_c, N - 1) * (q_d - q_b - 1)
        # 右
        answer += cum_sum_2d.range_sum(r_a, 0, r_c, r_d)
    # 縦だけ繰り返しあり
    elif q_a != q_c and q_b == q_d:
        # 上
        answer += cum_sum_2d.range_sum(r_a, r_b, N - 1, r_d)
        # 繰り返し
        answer += cum_sum_2d.range_sum(0, r_b, N - 1, r_d) * (q_c - q_a - 1)
        # 下
        answer += cum_sum_2d.range_sum(0, r_b, r_c, r_d)
    # 縦横繰り返しあり
    else:
        # 左上
        answer += cum_sum_2d.range_sum(r_a, r_b, N - 1, N - 1)
        # print(answer)
        # 上繰り返し
        answer += cum_sum_2d.range_sum(r_a, 0, N - 1, N - 1) * (q_d - q_b - 1)
        # print(answer)
        # 右上
        answer += cum_sum_2d.range_sum(r_a, 0, N - 1, r_d)
        # print(r_a, 0, N - 1, r_d)
        # print(answer)
        # 左繰り返し
        answer += cum_sum_2d.range_sum(0, r_b, N - 1, N - 1) * (q_c - q_a - 1)
        # 真ん中繰り返し
        answer += (
            cum_sum_2d.range_sum(0, 0, N - 1, N - 1) * (q_d - q_b - 1) * (q_c - q_a - 1)
        )
        # 右繰り返し
        answer += cum_sum_2d.range_sum(0, 0, N - 1, r_d) * (q_c - q_a - 1)
        # 左下
        answer += cum_sum_2d.range_sum(0, r_b, r_c, N - 1)
        # 下繰り返し
        answer += cum_sum_2d.range_sum(0, 0, r_c, N - 1) * (q_d - q_b - 1)
        # 右下
        answer += cum_sum_2d.range_sum(0, 0, r_c, r_d)
    print(answer)

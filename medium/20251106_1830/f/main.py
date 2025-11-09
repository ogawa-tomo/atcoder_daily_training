N, Q = map(int, input().split())


class Ball:
    def __init__(self, index: int, number: int):
        self.index = index  # 現在の位置
        self.number = number  # 書かれている番号


# balls[n]: 番号nのボール
balls = [Ball(i, i) for i in range(N)]

# ball_numbers[i]: i番目にあるボールの番号（number）
ball_numbers = list(range(N))
for _ in range(Q):
    x = int(input())
    x -= 1
    ball = balls[x]
    if ball.index < N - 1:
        right_index = ball.index + 1
    else:
        right_index = ball.index - 1
    right_ball = balls[ball_numbers[right_index]]

    # 入れ替え
    right_ball_index = right_ball.index
    right_ball.index = ball.index
    ball.index = right_ball_index

    ball_numbers[ball.index] = ball.number
    ball_numbers[right_ball.index] = right_ball.number
    # print(" ".join([str(n + 1) for n in ball_numbers]))


print(" ".join([str(n + 1) for n in ball_numbers]))

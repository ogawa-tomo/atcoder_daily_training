class Ball:
    def __init__(self, i: int, v: int) -> None:
        self.i = i
        self.v = v
        self.disabled = False


N, Q = map(int, input().split())
A = list(map(int, input().split()))
balls: list[Ball] = []
for i, a in enumerate(A):
    ball = Ball(i, a)
    balls.append(ball)

balls.sort(key=lambda b: b.v)

# inndex[i]: i番のボールがあるインデックス
index: dict[int, int] = {}
for i, ball in enumerate(balls):
    index[ball.i] = i


for q in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    for b in B:
        b -= 1
        ball_index = index[b]
        ball = balls[ball_index]
        ball.disabled = True
    for ball in balls:
        if not ball.disabled:
            print(ball.v)
            break
    for b in B:
        b -= 1
        ball_index = index[b]
        ball = balls[ball_index]
        ball.disabled = False

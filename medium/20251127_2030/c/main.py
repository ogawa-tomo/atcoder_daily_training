Q = int(input())
fukuro: list[int] = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        fukuro.append(x)
        fukuro.sort(reverse=True)
    elif q[0] == 2:
        ball = fukuro.pop(-1)
        print(ball)

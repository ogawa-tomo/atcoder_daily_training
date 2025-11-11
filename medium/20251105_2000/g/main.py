# 途中
N = int(input())


class Present:
    def __init__(self, p: int, a: int, b: int):
        self.p = p
        self.a = a
        self.b = b


max_p_a = 0
presents: list[Present] = []
for _ in range(N):
    p, a, b = map(int, input().split())
    presents.append(Present(p, a, b))
    max_p_a = max(max_p_a, p + a)

dp: list[list[int]] = []
for i in range(N):
    dp.append([0] * (max_p_a + 1))

for i in range(N - 1, -1, -1):
    present = presents[i]
    dp_i = dp[i]
    for j in range(max_p_a + 1):
        if i == N - 1:
            if present.p >= j:
                dp_i[j] = j + present.a
            else:
                dp_i[j] = max(0, j - present.b)
            continue
        if present.p >= j:
            dp_i[j] = dp[i + 1][j + present.a]
        else:
            dp_i[j] = dp[i + 1][max(0, j - present.b)]


Q = int(input())
for _ in range(Q):
    x = int(input())

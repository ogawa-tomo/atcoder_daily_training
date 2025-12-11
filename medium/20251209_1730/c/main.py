N, D = map(int, input().split())


class Sneak:
    def __init__(self, t: int, l: int):
        self.t = t
        self.l = l


sneaks: list[Sneak] = []
for _ in range(N):
    t, l = map(int, input().split())
    sneaks.append(Sneak(t, l))

for k in range(1, D + 1):
    max_weight = 0
    for sneak in sneaks:
        max_weight = max(max_weight, sneak.t * (sneak.l + k))
    print(max_weight)

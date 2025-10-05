class Base:
    def __init__(self, w: int, x: int):
        self.w = w
        self.x = x

    # 世界標準時tから始まる会議に参加できるかどうか
    def attendable(self, t: int):
        local_t = (t + self.x) % 24
        return 9 <= local_t and local_t <= 17


N = int(input())
bases: list[Base] = []
for _ in range(N):
    w, x = map(int, input().split())
    bases.append(Base(w, x))

answer = 0
for t in range(24):
    num = 0
    for base in bases:
        if base.attendable(t):
            num += base.w
    answer = max(answer, num)
print(answer)

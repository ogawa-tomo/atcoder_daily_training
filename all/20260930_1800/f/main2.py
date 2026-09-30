from fractions import Fraction


class Rope:
    def __init__(self, length: int, speed: int) -> None:
        if speed == 0:
            raise
        self.length = length
        self.speed = speed
        self.time = Fraction(self.length, self.speed)  # 燃やすのにかかる時間


N = int(input())

ropes: list[Rope] = []
for _ in range(N):
    a, b = map(int, input().split())
    rope = Rope(a, b)
    ropes.append(rope)

t = Fraction(0, 1)
for rope in ropes:
    t += rope.time
collide_time = Fraction(t, 2)

t = Fraction(0, 1)
p = Fraction(0, 1)
for rope in ropes:
    if t + rope.time > collide_time:
        p += (collide_time - t) * rope.speed
        print(float(p))
        exit()
    t += rope.time
    p += rope.length

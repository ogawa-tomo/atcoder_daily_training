from fractions import Fraction


class Rope:
    def __init__(self, length: int, speed: int) -> None:
        if speed == 0:
            raise
        self.length = length
        self.speed = speed
        self.time = Fraction(self.length, self.speed)  # 燃やすのにかかる時間
        self.left_t = Fraction(0, 1)  # 左から進んで左端に到達するまでの時間
        self.right_t = Fraction(0, 1)  # 右から進んで右端に到達するまでの時間

    def crosses(self):
        return (
            self.left_t + self.time >= self.right_t
            and self.right_t + self.time >= self.left_t
        )

    # クロスする地点
    def cross_point(self):
        if self.left_t <= self.right_t:
            left = (self.right_t - self.left_t) * self.speed
            return Fraction(left + self.length, 2)
        else:
            right = self.length - (self.left_t - self.right_t) * self.speed
            return Fraction(right, 2)


N = int(input())

ropes: list[Rope] = []
for _ in range(N):
    a, b = map(int, input().split())
    rope = Rope(a, b)
    ropes.append(rope)

t = Fraction(0, 1)
for rope in ropes:
    rope.left_t = t
    t += rope.time

ropes.reverse()
t = Fraction(0, 1)
for rope in ropes:
    rope.right_t = t
    t += rope.time
ropes.reverse()

current_point = 0
for rope in ropes:
    if rope.crosses():
        print(float(current_point + rope.cross_point()))
        exit()
    current_point += rope.length

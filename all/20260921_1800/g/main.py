import math

A, B = map(int, input().split())


def T(x: int):
    return A / ((1 + x) ** 0.5) + B * x


x = (A / (2 * B)) ** (2 / 3) - 1
x1 = math.floor(x)
x2 = math.ceil(x)
if x2 <= 0:
    print(T(0))
else:
    print(min(T(x1), T(x2)))

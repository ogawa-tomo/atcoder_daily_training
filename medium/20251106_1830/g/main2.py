# AC
import math


def ff(k):
    if k == 0:
        return 1
    return f(k // 2) + f(k // 3)


def f(k):
    if k <= 2:
        return ff(k)
    n = math.floor(math.log(k, 3))
    result = 0
    for x in range(n + 1):
        two_divide = n - x
        three_divide = x
        value = (k // (2**two_divide)) // (3**three_divide)
        result += f(value) * math.comb(n, x)
    return result


N = int(input())

print(f(N))

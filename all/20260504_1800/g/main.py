import sys

N = int(input())


def f(a: int, b: int):
    return a**3 + b * a**2 + a * b**2 + b**3


j = 10**6
X = sys.maxsize
for i in range(10**6):
    while f(i, j) >= N and j >= 0:
        X = min(X, f(i, j))
        j -= 1
print(X)

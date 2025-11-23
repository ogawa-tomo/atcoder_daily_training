import math

A, B = map(int, input().split())

r = math.sqrt(A**2 + B**2)

print(A / r, B / r)

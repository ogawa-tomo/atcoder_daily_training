import math

a, b, d = map(int, input().split())

r = math.radians(d)

x = math.cos(r) * a - math.sin(r) * b
y = math.sin(r) * a + math.cos(r) * b

print(x, y)

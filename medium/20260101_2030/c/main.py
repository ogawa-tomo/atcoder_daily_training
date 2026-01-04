import math

a, b, d = map(int, input().split())
theta = math.radians(d)
# print(math.cos(math.radians(60)))
x = a * math.cos(theta) - b * math.sin(theta)
y = a * math.sin(theta) + b * math.cos(theta)

print(x, y)

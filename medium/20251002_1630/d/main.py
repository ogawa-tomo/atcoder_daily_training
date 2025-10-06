import math

a, b, d = map(int, input().split())

radians = math.radians(d)
a_ = a * math.cos(radians) - b * math.sin(radians)
b_ = a * math.sin(radians) + b * math.cos(radians)

print(a_, b_)

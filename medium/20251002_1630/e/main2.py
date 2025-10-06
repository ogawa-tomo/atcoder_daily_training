import math
import sys

D = int(input())

answer = sys.maxsize
for x in range(math.ceil(math.sqrt(D))):
    y = math.sqrt(D - x**2)
    y_plus = math.ceil(y)
    y_minus = math.floor(y)
    answer = min(answer, abs(x**2 + y_plus**2 - D), abs(x**2 + y_minus**2 - D))
print(answer)

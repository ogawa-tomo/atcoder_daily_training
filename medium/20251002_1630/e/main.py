import math
import sys

D = int(input())

a = math.ceil(math.sqrt(D))

answer = sys.maxsize

while a >= 0:
    b_minus = math.floor(math.sqrt(abs(a**2 - D)))
    b_plus = math.ceil(math.sqrt(abs(a**2 - D)))
    answer = min(
        answer,
        abs(a**2 + b_minus**2 - D),
        abs(a**2 + b_plus**2 - D),
    )
    a -= 1


print(answer)

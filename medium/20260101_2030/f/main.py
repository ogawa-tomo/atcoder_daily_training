import math

N = int(input())
answer = 0
for a in range(1, 70):
    if 2**a > N:
        break
    b_target = N // (2**a)
    answer += (math.isqrt(b_target) + 1) // 2

print(answer)

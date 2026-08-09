import sys

N, S, M, L = map(int, input().split())

answer = sys.maxsize
for i in range(20):
    for j in range(20):
        for k in range(20):
            price = S * i + M * j + L * k
            num = 6 * i + 8 * j + 12 * k
            if num >= N:
                answer = min(answer, price)
print(answer)

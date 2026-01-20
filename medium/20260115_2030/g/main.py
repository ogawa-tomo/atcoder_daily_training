from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

# d[i][j]: 10^i倍すると余りがiになるAの数
d: list[defaultdict[int, int]] = []
for i in range(11):
    d.append(defaultdict(int))

for a in A:
    for i in range(11):
        num = a * 10**i
        m = num % M
        d[i][m] += 1

# print(d)
answer = 0
for a in A:
    length = len(str(a))
    m = a % M
    if m == 0:
        m = M
    answer += d[length][M - m]

print(answer)

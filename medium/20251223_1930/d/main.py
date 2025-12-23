M = int(input())
D = list(map(int, input().split()))

total = sum(D)
day = 0
for m in range(M):
    month = m + 1
    days = D[m]
    for d in range(days):
        day += 1
        if (total + 1) // 2 == day:
            print(month, d + 1)

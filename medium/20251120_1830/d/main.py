M = int(input())
D = list(map(int, input().split()))

all_days = sum(D)
half_day = all_days // 2
current_days = 0
for m in range(M):
    month_days = D[m]

    if current_days + month_days <= half_day:
        current_days += month_days
    else:
        day = half_day - current_days
        print(m + 1, day + 1)
        exit()

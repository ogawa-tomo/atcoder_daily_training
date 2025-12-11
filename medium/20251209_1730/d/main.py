N = int(input())
D = list(map(int, input().split()))

answer = 0
for i in range(N):
    month = i + 1
    days = D[i]
    for day in range(days):
        date = str(month) + str(day + 1)
        if len(set(list(date))) == 1:
            # print(date)
            answer += 1

print(answer)

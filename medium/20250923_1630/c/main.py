N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N + 1):
    count = 0
    for a in A:
        if a >= i:
            count += 1
    if count >= i:
        answer = i
print(answer)

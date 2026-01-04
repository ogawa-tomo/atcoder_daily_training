N = int(input())
A = list(map(int, input().split()))

A.sort()
answer = 0
i = 0
while True:
    if i >= N - 1:
        break
    if A[i] == A[i + 1]:
        answer += 1
        i += 2
    else:
        i += 1


print(answer)

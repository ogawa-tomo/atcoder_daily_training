N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(2 * N - 2):
    if A[i] == A[i + 2]:
        answer += 1

print(answer)

N, P = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for n in A:
    if n < P:
        answer += 1

print(answer)

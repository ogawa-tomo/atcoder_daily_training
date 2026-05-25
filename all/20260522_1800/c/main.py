N = int(input())
A = list(map(int, input().split()))

answer = list(set(A))
answer.sort()
print(len(answer))
print(*answer)

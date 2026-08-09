N = int(input())
A = list(map(int, input().split()))

max_index = 0
for i in range(N):
    a = A[i]
    if i > max_index:
        break
    max_index = max(max_index, i + a - 1)

print(min(N, max_index + 1))

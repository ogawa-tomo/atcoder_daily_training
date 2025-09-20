N = int(input())
H = list(map(int, input().split()))

answer = H[0]
for i in range(N):
    if i == N - 1:
        break
    h = H[i]
    next_h = H[i + 1]
    if next_h <= h:
        break
    answer = next_h

print(answer)

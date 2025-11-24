N = int(input())
L = list(map(int, input().split()))

if 1 not in L:
    print(0)
    exit()

for i in range(N):
    l = L[i]
    if l:
        left_reachable_rooms = i + 1
        break

for i in range(N - 1, -1, -1):
    l = L[i]
    if l:
        right_reachable_rooms = N + 1 - i - 1
        break

print(N + 1 - left_reachable_rooms - right_reachable_rooms)

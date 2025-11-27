N, A = map(int, input().split())
T = list(map(int, input().split()))

t = 0
for i in range(N):
    start_time = max(t, T[i])
    t = start_time + A
    print(t)

N, T = map(int, input().split())
A = list(map(int, input().split()))

cycle = sum(A)
T %= cycle

time = 0
for i, a in enumerate(A):
    time += a
    if time >= T:
        print(i + 1, a - (time - T))
        exit()

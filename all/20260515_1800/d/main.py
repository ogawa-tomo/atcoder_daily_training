T, X = map(int, input().split())
A = list(map(int, input().split()))

saved = 0
for t in range(T + 1):
    a = A[t]
    if t == 0:
        saved = a
        print(t, a)
        continue
    if abs(saved - a) >= X:
        saved = a
        print(t, a)

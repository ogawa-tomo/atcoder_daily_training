Q = int(input())

A: list[int] = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        A.append(x)
    elif q[0] == 2:
        k = q[1]
        print(A[len(A) - k])

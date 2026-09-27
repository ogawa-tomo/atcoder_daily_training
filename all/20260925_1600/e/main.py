N, Q = map(int, input().split())
A = [i + 1 for i in range(N)]
start_index = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        p = q[1]
        p -= 1
        x = q[2]
        A[(start_index + p) % N] = x
    elif q[0] == 2:
        p = q[1]
        p -= 1
        print(A[(start_index + p) % N])
    elif q[0] == 3:
        k = q[1]
        start_index += k

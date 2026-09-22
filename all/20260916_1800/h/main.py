# WA
N, M = map(int, input().split())
A = [0] * N
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if x == y and z != 0:
        print(-1)
        exit()
    ax = A[x]
    ay = A[y]
    if A[x] == 0:
        A[y] = z
    elif A[y] == 0:
        A[x] = z
    else:
        if A[x] ^ A[y] != z:
            print(-1)
            exit()

print(*A)

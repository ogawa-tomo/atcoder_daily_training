N, Q = map(int, input().split())

A_list: list[list[int]] = []
for _ in range(N):
    AL = list(map(int, input().split()))
    L = AL[0]
    A = AL[1:]
    # print(L, A)
    A_list.append(A)

for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    print(A_list[s][t])

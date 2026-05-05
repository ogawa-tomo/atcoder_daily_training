N, T = map(int, input().split())
A = list(map(int, input().split()))

r_dict: dict[int, list[int]] = {}
c_dict: dict[int, list[int]] = {}
d1_list: list[int] = []
d2_list: list[int] = []
for i in range(N):
    r_dict[i] = []
    c_dict[i] = []

for i, a in enumerate(A):
    a -= 1
    r = a // N
    c = a % N
    r_dict[r].append(a)
    c_dict[c].append(a)
    if r == c:
        d1_list.append(a)
    if r + c == N - 1:
        d2_list.append(a)
    if (
        len(r_dict[r]) == N
        or len(c_dict[c]) == N
        or len(d1_list) == N
        or len(d2_list) == N
    ):
        print(i + 1)
        exit()
print(-1)

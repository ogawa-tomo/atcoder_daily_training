S = list(map(int, list(input())))
# print(S)
N = len(S)

A_num = N

B_num = 0
for i in range(N):
    d = S[N - 1 - i]
    d -= B_num
    d %= 10
    B_num += d

print(A_num + B_num)

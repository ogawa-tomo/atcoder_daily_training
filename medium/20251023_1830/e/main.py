N, T = map(int, input().split())
A = list(map(int, input().split()))


def get_i(number: int):
    return (number - 1) // N + 1


def get_j(number: int):
    return (number - 1) % N + 1


# row[i]: i行目で空いたマスの数
row = [0] * (N + 1)
# column[j]: j列目で空いたマスの数
column = [0] * (N + 1)

# 左上・右下の対角で空いたマスの数
diagonal1 = 0
# 左下・右上の対角で空いたマスの数
diagonal2 = 0

for t in range(T):
    a = A[t]
    turn = t + 1
    i = get_i(a)
    j = get_j(a)
    row[i] += 1
    if row[i] == N:
        print(turn)
        exit()
    column[j] += 1
    if column[j] == N:
        print(turn)
        exit()
    if i == j:
        diagonal1 += 1
        if diagonal1 == N:
            print(turn)
            exit()
    if i + j == N + 1:
        diagonal2 += 1
        if diagonal2 == N:
            print(turn)
            exit()
print(-1)

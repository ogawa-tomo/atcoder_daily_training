N, X = map(int, input().split())

bags: list[list[int]] = []
for _ in range(N):
    d = list(map(int, input().split()))
    L = d[0]
    A = d[1:]
    # print(L, A)
    bags.append(A)


# for bag in bags:


# i番目の袋を開ける前の時点で値がcurrent_valueのとき、条件を満たすパターンの数
def dfs(current_value: int, i: int):
    if i == N:
        if current_value == X:
            return 1
        else:
            return 0
    bag = bags[i]
    num = 0
    for ball in bag:
        num += dfs(current_value * ball, i + 1)
    return num


answer = dfs(1, 0)
print(answer)

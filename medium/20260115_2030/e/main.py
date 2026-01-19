from collections import deque

N, A, B = map(int, input().split())
S = deque(list(input()))
# print(S)


def cost_by_2(s: deque[str]):
    length = len(s)
    half = length // 2
    cost = 0
    for i in range(half):
        if s[i] != s[length - 1 - i]:
            cost += B
    return cost


answer = cost_by_2(S)
for i in range(N):
    c = (i + 1) * A
    S.append(S.popleft())
    # print(S)
    answer = min(answer, c + cost_by_2(S))

print(answer)

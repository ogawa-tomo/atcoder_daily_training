# AC
N, S = map(int, input().split())
A = list(map(int, input().split()))

d: dict[int, int] = {}

answer = 0
for a in A:
    target = S - a
    if target in d:
        answer += d[target]
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(answer)

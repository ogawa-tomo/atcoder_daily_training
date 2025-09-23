N = int(input())
d: dict[str, int] = {}

for _ in range(N):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

max_vote = 0
answer = ""
for name in d:
    # print(name)
    if d[name] > max_vote:
        answer = name
        max_vote = d[name]

print(answer)

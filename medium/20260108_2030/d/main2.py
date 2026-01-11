N = int(input())
M = 0
S: list[list[str]] = []
for _ in range(N):
    s = list(input())
    S.append(s)
    M = max(M, len(s))

# S.reverse()
# print(S)

answer: list[list[str]] = []
for _ in range(M):
    answer.append(["*"] * N)

# print(answer)
for i, s in enumerate(S):
    for j, c in enumerate(s):
        answer[j][N - 1 - i] = c

for a in answer:
    while a[-1] == "*":
        a.pop()
    print("".join(a))

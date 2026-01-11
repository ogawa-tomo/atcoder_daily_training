N = int(input())
M = 0
S: list[list[str]] = []
for _ in range(N):
    s = list(input())
    S.append(s)
    M = max(M, len(s))

# print(S)

answers: list[list[str]] = []
for i in range(M):
    row: list[str] = []
    appeared = False
    for s in S:
        if i <= len(s) - 1:
            appeared = True
            row.append(s[i])
        else:
            if appeared:
                row.append("*")
    row.reverse()
    answers.append(row)

for a in answers:
    print("".join(a))

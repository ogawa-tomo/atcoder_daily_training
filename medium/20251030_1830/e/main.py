N = int(input())
S = list(input())

bundled = False
answer: list[str] = []
for s in S:
    if s == '"':
        bundled = not bundled
        answer.append(s)
    elif s == "," and not bundled:
        answer.append(".")
    else:
        answer.append(s)

print("".join(answer))

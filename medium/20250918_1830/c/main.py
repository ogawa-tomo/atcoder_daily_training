S = list(input())

T: list[str] = []

for i in range(len(S)):
    s = S[i]
    if s == "#":
        T.append("#")
        continue
    if i == 0:
        T.append("o")
        continue
    if S[i - 1] == "#":
        T.append("o")
    else:
        T.append(".")

print("".join(T))

S = list(input())
T = list(input())


N = len(S)

X: list[str] = []

while S != T:
    next_S = "z" * N
    for i in range(N):
        s = S[i]
        t = T[i]
        if s != t:
            candidate = S.copy()
            candidate[i] = t
            next_S = min(next_S, "".join(candidate))
    X.append("".join(next_S))
    S = list(next_S)

print(len(X))
for x in X:
    print(x)

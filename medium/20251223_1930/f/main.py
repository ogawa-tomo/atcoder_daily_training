S = list(input())
T = list(input())


N = len(S)

X: list[str] = []
for i in range(N):
    s = S[i]
    t = T[i]
    if s > t:
        S[i] = t
        X.append("".join(S))

for i in range(N - 1, -1, -1):
    s = S[i]
    t = T[i]
    if s < t:
        S[i] = t
        X.append("".join(S))

print(len(X))
for x in X:
    print(x)

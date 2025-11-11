S = list(input())
T = list(input())

X: list[list[str]] = []

N = len(S)
for i in range(N):
    s = S[i]
    t = T[i]
    if s > t:
        S[i] = t
        X.append(S.copy())
for i in range(N - 1, -1, -1):
    s = S[i]
    t = T[i]
    if s < t:
        S[i] = t
        X.append(S.copy())

print(len(X))
for x in X:
    print("".join(x))

N, D = map(int, input().split())
S = list(input())

cookie_indice: list[int] = []
for i in range(N):
    if S[i] == "@":
        cookie_indice.append(i)

cookie_indice.reverse()
for d in range(D):
    if d >= len(cookie_indice):
        break
    S[cookie_indice[d]] = "."

print("".join(S))

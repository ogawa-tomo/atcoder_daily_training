S = list(input())
N = len(S)

strings: list[str] = []
for i in range(N):
    S = [*S[1:], S[0]]
    strings.append("".join(S))

# print(strings)
strings.sort()
print(strings[0])
print(strings[N - 1])

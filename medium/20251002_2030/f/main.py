N, K, X = map(int, input().split())
S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

# print(S)

strings: list[str] = []
for i in range(N**K):
    string = ""
    # K桁目
    for k in range(K):
        string += S[(i // N**k) % N]
    strings.append(string)

strings.sort()
# print(strings)

print(strings[X - 1])

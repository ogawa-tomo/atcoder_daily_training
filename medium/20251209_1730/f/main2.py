N, K, X = map(int, input().split())

strings: list[str] = []
for _ in range(N):
    s = input()
    strings.append(s)

f_strings: list[str] = []


def dfs(string: str, count: int):
    if count == K:
        return f_strings.append(string)
    for s in strings:
        dfs(string + s, count + 1)


dfs("", 0)
# print(f_strings)
f_strings.sort()
print(f_strings[X - 1])

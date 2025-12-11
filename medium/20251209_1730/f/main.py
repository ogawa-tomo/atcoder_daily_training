N, K, X = map(int, input().split())

strings: list[str] = []
for _ in range(N):
    s = input()
    strings.append(s)

f_strings: list[str] = []
for i in range(N**K):
    # i: N進法のK桁の数字
    f_string: str = ""
    for k in range(K):
        # k桁目の数字
        d = (i % (N ** (k + 1))) // (N**k)
        f_string += strings[d]
    f_strings.append(f_string)

# print(f_strings)
f_strings.sort()
print(f_strings[X - 1])

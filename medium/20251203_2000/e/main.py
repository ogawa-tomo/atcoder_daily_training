N = int(input())

strings: set[str] = set()
for _ in range(N):
    s_list = list(input())
    reverse_s_list = list(reversed(s_list))

    s = "".join(s_list)
    reverse_s = "".join(reverse_s_list)
    # string = sorted([s, reverse_s])[0]
    string = min(s, reverse_s)
    # print(string)
    # print(s, reverse_s)
    strings.add(string)

print(len(strings))

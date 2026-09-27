from collections import defaultdict

S = input()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# num[s]: いまいる地点より前でsが登場した回数
num: defaultdict[str, int] = defaultdict(int)

# d[s]: 次にsが登場したときにできる回文の数
d: defaultdict[str, int] = defaultdict(int)

answer = 0
for i, s in enumerate(S):
    answer += d[s]
    for alphabet in alphabets:
        d[alphabet] += num[alphabet]

    if i > 0:
        prev_s = S[i - 1]
        num[prev_s] += 1
        d[prev_s] += 1

print(answer)

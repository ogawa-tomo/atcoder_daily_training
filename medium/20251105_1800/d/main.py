from collections import defaultdict

S = list(input())

d: defaultdict[str, int] = defaultdict(int)

for i in range(26):
    s = S[i]
    d[s] = i
# print(d)

alphabets = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
distance = 0
current_i = d["A"]
for alphabet in alphabets:
    distance += abs(current_i - d[alphabet])
    current_i = d[alphabet]

print(distance)

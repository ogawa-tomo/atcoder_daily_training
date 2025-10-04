S = list(input())
T = list(input())
N = len(S)

for i in range(N):
    s = S[i]
    t = T[i]
    if i == 0:
        diff = (ord(t) - ord(s)) % 26
        continue
    if (ord(t) - ord(s)) % 26 != diff:
        print("No")
        exit()
print("Yes")

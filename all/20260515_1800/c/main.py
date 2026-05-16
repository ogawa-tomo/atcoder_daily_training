S = list(input())
T = list(input())

N = len(S)

for k in range(26):
    ok = True
    for i in range(N):
        s = S[i]
        t = T[i]

        t_ord = ord(t) + k
        if t_ord >= 123:
            t_ord -= 26
        new_t = chr(t_ord)
        # print(s, new_t)
        if s != new_t:
            ok = False
            break
    if ok:
        print("Yes")
        exit()
print("No")

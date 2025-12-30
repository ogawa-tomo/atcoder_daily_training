T = list(input())
U = list(input())

lenT = len(T)
lenU = len(U)

for i in range(lenT - lenU + 1):
    ok = True
    for j in range(lenU):
        t = T[i + j]
        u = U[j]
        if t != "?" and t != u:
            ok = False
            break
    if ok:
        print("Yes")
        exit()

print("No")

K = int(input())
S = input()
T = input()

lenS = len(S)
lenT = len(T)

if lenS == lenT:
    count = 0
    for i in range(lenS):
        if S[i] != T[i]:
            if count > 0:
                print("No")
                exit()
            count += 1
    print("Yes")
elif lenS == lenT + 1:
    si = 0
    ti = 0
    while True:
        if S[si] != T[ti]:
            if si > ti:
                print("No")
                exit()
            si += 1
            if S[si] != T[ti]:
                print("No")
                exit()
        si += 1
        ti += 1
        if si >= lenS or ti >= lenT:
            print("Yes")
            exit()
elif lenS == lenT - 1:
    si = 0
    ti = 0
    while True:
        if S[si] != T[ti]:
            if ti > si:
                print("No")
                exit()
            ti += 1
            if S[si] != T[ti]:
                print("No")
                exit()
        si += 1
        ti += 1
        if si >= lenS or ti >= lenT:
            print("Yes")
            exit()
else:
    print("No")

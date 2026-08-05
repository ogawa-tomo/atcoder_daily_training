S = input()
T = input()

for i in range(len(S)):
    if i == 0:
        continue
    s = S[i]
    if s.isupper():
        target = S[i - 1]
        if target not in T:
            print("No")
            exit()

print("Yes")

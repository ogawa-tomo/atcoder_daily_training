S = input()
T = input()
N = len(S)

if S == T:
    print("Yes")
    exit()

for i in range(N - 1):
    new_S = list(S)
    new_S[i] = S[i + 1]
    new_S[i + 1] = S[i]
    if "".join(new_S) == T:
        print("Yes")
        exit()

print("No")

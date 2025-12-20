S = list(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

if len(S) != 8:
    print("No")
    exit()

for i in range(8):
    s = S[i]
    if i == 0 or i == 7:
        if s not in alphabets:
            print("No")
            exit()
    elif i == 1:
        if s in alphabets or s == "0":
            print("No")
            exit()
    else:
        if s not in nums:
            print("No")
            exit()

print("Yes")

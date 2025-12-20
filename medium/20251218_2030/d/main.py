# WA
# Sがアルファベット1文字でYesにしてしまう
S = list(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
current = "l"  # "l" or "n"
num_count = 0
for s in S:
    if current == "l":
        if s not in alphabets:
            print("No")
            exit()
        current = "n"
    elif current == "n":
        if num_count == 0:
            if s in alphabets or s == "0":
                print("No")
                exit()
        else:
            if s not in nums:
                print("No")
                exit()
        num_count += 1
        if num_count == 6:
            current = "l"
            num_count = 0

if s in alphabets:
    print("Yes")
else:
    print("No")

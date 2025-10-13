S = list(input())
T = list(input())

length = len(S)

for i in range(length - 1):
    next_letter = S[i + 1]
    if next_letter.islower():
        continue
    current_letter = S[i]
    if not current_letter in T:
        print("No")
        exit()
print("Yes")

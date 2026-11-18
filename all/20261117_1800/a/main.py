S = input()

answer = -1
for i in range(len(S)):
    s = S[i]
    if s == "a":
        answer = i + 1

print(answer)

S = list(input())

current = "i"
answer = 0
for s in S:
    if s != current:
        answer += 1
    else:
        if current == "i":
            current = "o"
        else:
            current = "i"
if s == "i":
    answer += 1

print(answer)

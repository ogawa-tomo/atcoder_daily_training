S = list(input())

current = "A"
for s in S:
    if s == "A":
        if current != "A":
            print("No")
            exit()
    elif s == "B":
        if current == "C":
            print("No")
            exit()
    elif s == "C":
        pass
    current = s

print("Yes")

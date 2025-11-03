X = list(input())

length = len(X)

for i in range(3):
    if X[length - i - 1] != "0":
        break
    X.pop(length - i - 1)

if X[-1] == ".":
    X.pop(-1)
print("".join(X))

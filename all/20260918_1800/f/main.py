N = int(input())
A = list(map(int, input().split()))

row: list[int] = []
for a in A:
    # print(row)
    row.append(a)
    while True:
        if len(row) <= 1:
            break
        if row[-1] != row[-2]:
            break
        new = row[-1] + 1
        row.pop()
        row.pop()
        row.append(new)

# print(row)
print(len(row))

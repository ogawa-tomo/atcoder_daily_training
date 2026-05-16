N = int(input())
A = list(map(int, input().split()))
column: list[int] = []
for a in A:
    column.append(a)
    while True:
        length = len(column)
        if length <= 1:
            break
        first = column[length - 1]
        second = column[length - 2]
        if first != second:
            break
        column.pop()
        column.pop()
        column.append(first + 1)

print(len(column))

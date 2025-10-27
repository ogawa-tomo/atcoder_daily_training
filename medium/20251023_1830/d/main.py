N = int(input())

grids: list[list[str]] = []
for _ in range(N):
    row = list(input())
    grids.append(row)

# print(grids)

x = [1, 1, 0, -1, -1, -1, 0, 1]
y = [0, 1, 1, 1, 0, -1, -1, -1]

answer = 0
for i in range(N):
    for j in range(N):
        for d in range(8):
            xd = x[d]
            yd = y[d]
            number = ""
            for k in range(N):
                number += grids[(i + xd * k) % N][(j + yd * k) % N]
            answer = max(int(number), answer)

print(answer)

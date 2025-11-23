N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):
    distances: list[int] = []
    for j in range(i + 1, N):
        distance = 0
        for k in range(i, j):
            distance += D[k]
        distances.append(distance)
    print(*distances)

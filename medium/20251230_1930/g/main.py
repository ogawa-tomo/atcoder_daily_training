N = int(input())
A = [0] + list(map(int, input().split()))

# left[i]: iを右端とする最長の左ピラミッド数列の長さ
left = [0] * (N + 2)

# right[i]: iを左端とする最長の右ピラミッド数列の長さ
right = [0] * (N + 2)


for i in range(1, N + 1):
    left[i] = min(A[i], left[i - 1] + 1)

for i in range(N, 0, -1):
    right[i] = min(A[i], right[i + 1] + 1)


# pyramids[i]: iを頂点とするピラミッドの高さ
pyramids = [min(left[i], right[i]) for i in range(1, N + 1)]

print(max(pyramids))

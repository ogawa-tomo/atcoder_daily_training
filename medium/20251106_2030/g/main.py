N, M = map(int, input().split())
X = list(map(int, input().split()))

# 家のある座標を並べたもの
house_positions = list(set(X))
house_positions.sort()
# print(house_positions)

# 家のある座標の数が、基地局数より少なければ、各家の位置に基地局を置いて終わり
if len(house_positions) <= M:
    print(0)
    exit()

# 家の隙間を並べたもの
house_distances: list[int] = []
for i in range(1, len(house_positions)):
    house_distances.append(house_positions[i] - house_positions[i - 1])
house_distances.sort(reverse=True)
# print(house_distances)

# 2個目の基地局を置ければ、隙間を1つ消せる
answer = sum(house_distances)
for i in range(M - 1):
    answer -= house_distances[i]
print(answer)

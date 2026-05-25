N, Q = map(int, input().split())
X = list(map(int, input().split()))

boxes = [0] * N
# print(boxes)
answer: list[int] = []
for i, x in enumerate(X):
    if x >= 1:
        boxes[x - 1] += 1
        answer.append(x)
    else:
        min_num = min(boxes)
        for j, box in enumerate(boxes):
            if box == min_num:
                boxes[j] += 1
                answer.append(j + 1)
                break
print(*answer)

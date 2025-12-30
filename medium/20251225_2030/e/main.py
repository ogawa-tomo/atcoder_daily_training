N = int(input())
Q = int(input())

# cards_by_box[i]: 箱iに入っているカードのリスト
cards_by_box: list[list[int]] = []
for _ in range(N + 1):
    cards_by_box.append([])

# boxes_by_card[i]: カードiが入っている箱のセット
boxes_by_card: list[set[int]] = []
for _ in range(2 * 10**5 + 1):
    boxes_by_card.append(set())

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        cards_by_box[j].append(i)
        boxes_by_card[i].add(j)
    elif q[0] == 2:
        i = q[1]
        cards_by_box[i].sort()
        print(*cards_by_box[i])
    elif q[0] == 3:
        i = q[1]
        boxes = list(boxes_by_card[i])
        boxes.sort()
        print(*boxes)

class Box:
    def __init__(self, i: int) -> None:
        self.i = i
        self.cards: list[int] = []

    def __lt__(self, other):
        if not isinstance(other, Box):
            raise
        return self.i < other.i


N = int(input())

boxes = [Box(i) for i in range(N)]
boxes_by_card: dict[int, set[Box]] = {}
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        j -= 1
        box = boxes[j]
        box.cards.append(i)
        if i not in boxes_by_card:
            boxes_by_card[i] = set()
        boxes_by_card[i].add(box)

    elif q[0] == 2:
        i = q[1]
        box = boxes[i - 1]
        box.cards.sort()
        print(*box.cards)
    elif q[0] == 3:
        i = q[1]
        target_boxes = list(boxes_by_card[i])
        target_boxes.sort()
        print(*[str(box.i + 1) for box in target_boxes])

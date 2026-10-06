from collections import defaultdict


class Potion:
    def __init__(self) -> None:
        self.used = False


class Event:
    def __init__(self, potion: Potion | None, use_potion: bool) -> None:
        self.potion = potion
        self.use_potion = use_potion


N = int(input())

# portions[x]: 拾ったポーションxのリスト
potions_by_x: defaultdict[int, list[Potion]] = defaultdict(list)
events: list[Event] = []
for i in range(N):
    t, x = map(int, input().split())
    if t == 1:
        potion = Potion()
        potions_by_x[x].append(potion)
        event = Event(potion, False)
        events.append(event)
    elif t == 2:
        x_potions = potions_by_x[x]
        if not x_potions:
            print(-1)
            exit()
        potion = x_potions.pop()
        potion.used = True
        event = Event(None, True)
        events.append(event)

answers: list[int] = []
potion_num = 0
max_potion_num = 0
for event in events:
    if event.potion is not None:
        if event.potion.used:
            answers.append(1)
            potion_num += 1
            max_potion_num = max(max_potion_num, potion_num)
        else:
            answers.append(0)
    elif event.use_potion:
        potion_num -= 1

print(max_potion_num)
print(*answers)

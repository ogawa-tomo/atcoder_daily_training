from collections import defaultdict


class Event:
    def __init__(self, t: int, x: int) -> None:
        self.t = t
        self.x = x
        self.get = False  # このイベントでポーションを取るか


N = int(input())

events: list[Event] = []
for _ in range(N):
    t, x = map(int, input().split())
    event = Event(t, x)
    events.append(event)

events.reverse()
# needed[x]: ポーションxの必要量
needed: defaultdict[int, int] = defaultdict(int)
for event in events:
    if event.t == 1:
        if needed[event.x] > 0:
            needed[event.x] -= 1
            event.get = True
    elif event.t == 2:
        needed[event.x] += 1

# print(needed)
for n in needed.values():
    if n > 0:
        print(-1)
        exit()

events.reverse()
potion_num = 0
max_potion_num = 0
answers: list[int] = []
for event in events:
    if event.t == 1:
        if event.get:
            potion_num += 1
            max_potion_num = max(max_potion_num, potion_num)
            answers.append(1)
        else:
            answers.append(0)
    elif event.t == 2:
        potion_num -= 1

print(max_potion_num)
print(*answers)

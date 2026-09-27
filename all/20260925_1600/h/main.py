# WA
from fractions import Fraction


class Card:
    def __init__(self, value: int, cost: int) -> None:
        self.value = value
        self.cost = cost
        self.performance = Fraction(self.value, self.cost)

    def __repr__(self) -> str:
        return str((self.value, self.cost))


N = int(input())
C = list(map(int, input().split()))

cards: list[Card] = []
# emerged: set[int] = set()
for i in range(8, -1, -1):
    value = i + 1
    cost = C[i]
    # if cost in emerged:
    #     continue
    cards.append(Card(value, cost))
    # emerged.add(cost)

cards.sort(key=lambda c: c.performance, reverse=True)
# print(cards)

x = 0
cost = 0
while True:
    budget = N - cost
    best_card: Card | None = None
    best_x = x
    best_cost = 0
    for card in cards:
        count = budget // card.cost  # cardを何回使えるか
        new_x = int(str(x) + str(card.value) * count)
        if new_x > best_x:
            best_x = new_x
            best_card = card
            best_cost = card.cost * count

    print(best_x)
    if best_card is None:
        break
    x = best_x
    cost += best_cost

print(x)

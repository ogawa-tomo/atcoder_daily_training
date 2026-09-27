# WA
class Card:
    def __init__(self, value: int, cost: int) -> None:
        self.value = value
        self.cost = cost

    def __repr__(self) -> str:
        return str((self.value, self.cost))


N = int(input())
C = list(map(int, input().split()))

cards: list[Card] = []
for i in range(9):
    value = i + 1
    cost = C[i]
    cards.append(Card(value, cost))


# 現在x、budgetの状態のとき、得られるxの最大値
def dfs(x: int, budget: int):
    best_x = x
    for card in cards:
        count = budget // card.cost
        if count == 0:
            continue
        next_x = int(str(x) + str(card.value) * count)
        next_budget = budget - card.cost * count
        best_x = max(best_x, dfs(next_x, next_budget))
    return best_x


x = dfs(0, N)
print(x)

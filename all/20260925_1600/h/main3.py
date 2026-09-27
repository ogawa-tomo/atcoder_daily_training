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

cards.sort(key=lambda c: c.cost)
min_cost_card = cards[0]

# 最大の桁数を確保するため、最小コストのカードをできるだけ適用する
digit_num = N // min_cost_card.cost
card_list = [min_cost_card] * digit_num

# 上の桁から順に可能な限り大きな数字に置き換える
cost = min_cost_card.cost * digit_num
cards.sort(key=lambda c: c.value, reverse=True)
for digit in range(digit_num):
    current_card = card_list[digit]
    for card in cards:
        if (
            card.value > current_card.value
            and cost - current_card.cost + card.cost <= N
        ):
            card_list[digit] = card
            cost += card.cost - current_card.cost
            break

print(int("".join([str(card.value) for card in card_list])))

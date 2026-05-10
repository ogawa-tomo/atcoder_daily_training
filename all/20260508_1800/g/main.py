N = int(input())
mod = 998244353


class Card:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.a_num = 0
        self.b_num = 0


cards: list[Card] = []
for _ in range(N):
    a, b = map(int, input().split())
    card = Card(a, b)
    cards.append(card)
# n = 10**5
# print(2**n)

cards[0].a_num = 1
cards[0].b_num = 1
for i in range(N - 1):
    current_card = cards[i]
    next_card = cards[i + 1]
    if current_card.a != next_card.a:
        next_card.a_num += current_card.a_num
    if current_card.a != next_card.b:
        next_card.b_num += current_card.a_num
    if current_card.b != next_card.a:
        next_card.a_num += current_card.b_num
    if current_card.b != next_card.b:
        next_card.b_num += current_card.b_num
    next_card.a_num %= mod
    next_card.b_num %= mod

print((cards[N - 1].a_num + cards[N - 1].b_num) % mod)

class Card:
    def __init__(self, front: int, back: int) -> None:
        self.front = front
        self.back = back
        self.is_front = True

    @property
    def value(self):
        return self.front if self.is_front else self.back

    @property
    def reverse_effect(self):
        if self.is_front:
            return self.back - self.front
        else:
            return self.front - self.back

    def reverse(self):
        self.is_front = not self.is_front


N, K = map(int, input().split())

cards: list[Card] = []
for _ in range(N):
    a, b = map(int, input().split())
    card = Card(a, b)
    cards.append(card)

for _ in range(K):
    # K回の繰り返しごとに、最大の効果のある反転区間を求める
    right = 0
    max_effect = 0  # 0のままなら何も返さないのが最善
    max_effect_left = 0
    max_effect_right = 0
    current_effect = 0

    for left in range(N):
        left_card = cards[left]
        if left_card.reverse_effect <= 0:
            # 反転効果が負のカードを左端に置く意味はない
            continue
        if right <= left:
            # leftが追い越したらリセット
            right = left
            current_effect = left_card.reverse_effect
        while True:
            if current_effect > max_effect:
                max_effect = current_effect
                max_effect_left = left
                max_effect_right = right
            if right >= N - 1:
                break
            # 効果が正である限り、区間を右に伸ばし続ける
            next_card = cards[right + 1]
            if current_effect + next_card.reverse_effect > 0:
                right += 1
                current_effect += next_card.reverse_effect
            else:
                break

        # leftが1増えるとき、区間からカードが減るので効果に影響することに注意
        current_effect -= left_card.reverse_effect

    if max_effect > 0:
        for i in range(max_effect_left, max_effect_right + 1):
            card = cards[i]
            card.reverse()

answer = 0
for card in cards:
    answer += card.value
print(answer)

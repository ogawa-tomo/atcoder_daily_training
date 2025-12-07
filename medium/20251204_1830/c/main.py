import sys

N = int(input())


class Person:
    def __init__(self, i: int, bet: set[int]):
        self.i = i
        self.bet = bet


people: list[Person] = []
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    person = Person(i, set(A))
    people.append(person)

X = int(input())
min_bet_num = sys.maxsize
for person in people:
    if X in person.bet:
        min_bet_num = min(min_bet_num, len(person.bet))

answer: list[int] = []
for person in people:
    if X in person.bet and len(person.bet) == min_bet_num:
        answer.append(person.i + 1)

print(len(answer))
print(*answer)

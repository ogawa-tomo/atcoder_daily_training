import sys

N = int(input())
S = list(map(int, list(input())))
W = list(map(int, input().split()))
# print(S)


class Person:
    def __init__(self, weight: int, is_adult: bool):
        self.weight = weight
        self.is_adult = is_adult

    def __lt__(self, other):
        return self.weight < other.weight


people: list[Person] = []
num_adults = 0
num_children = 0
for i in range(N):
    is_adult = bool(S[i])
    weight = W[i]
    person = Person(weight, is_adult)
    people.append(person)
    if is_adult:
        num_adults += 1
    else:
        num_children += 1

people.sort()


correct_children = 0
correct_adults = num_adults
answer = correct_children + correct_adults
for i in range(N):
    person = people[i]
    if person.is_adult:
        correct_adults -= 1
    else:
        correct_children += 1
    if i == N - 1 or person.weight != people[i + 1].weight:
        answer = max(answer, correct_adults + correct_children)

print(answer)

# WA
import copy


class Person:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)


N = int(input())

A: list[list[int]] = []
for _ in range(2 * N - 1):
    A.append(list(map(int, input().split())))


def score(p1: Person, p2: Person) -> int:
    i = min(p1.i, p2.i)
    j = max(p1.i, p2.i)
    return A[i][j - i - 1]


scores: list[int] = []


# 残っている人のリストを与えたとき、そこで最大のスコアを返す
# 排他的論理和の演算は単調増加ではないので意味がない
def max_score(remaining_people: list[Person]):
    if len(remaining_people) == 2:
        p1 = remaining_people[0]
        p2 = remaining_people[1]
        return score(p1, p2)

    remaining_people = copy.copy(remaining_people)
    person1 = remaining_people.pop()
    result = 0
    for remaining_person in remaining_people:
        pair_score = score(person1, remaining_person)
        new_remaining_people = copy.copy(remaining_people)
        new_remaining_people.remove(remaining_person)
        result = max(result, pair_score ^ max_score(new_remaining_people))
    return result


people = [Person(i) for i in range(2 * N)]


print(max_score(people))

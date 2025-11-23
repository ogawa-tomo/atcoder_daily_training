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


all_people: list[Person] = []
adults: list[Person] = []
children: list[Person] = []

for i in range(N):
    is_adult = bool(S[i])
    weight = W[i]
    person = Person(weight, is_adult)
    all_people.append(person)
    if is_adult:
        adults.append(person)
    else:
        children.append(person)

all_people.sort()
adults.sort()
children.sort()

thresholds = [p.weight for p in all_people]
thresholds.append(sys.maxsize)
num_adults = len(adults)
num_children = len(children)


# print(thresholds)
def num_adults_lighter_than(weight: int):
    ok = -1
    ng = num_adults
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if adults[mid].weight < weight:
            ok = mid
        else:
            ng = mid
    return ok + 1


def num_children_lighter_than(weight: int):
    ok = -1
    ng = num_children
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if children[mid].weight < weight:
            ok = mid
        else:
            ng = mid
    return ok + 1


answer = 0
for threshold in thresholds:
    correct_children = num_children_lighter_than(threshold)
    correct_adults = num_adults - num_adults_lighter_than(threshold)
    answer = max(answer, correct_children + correct_adults)
print(answer)

import sys


class Person:
    def __init__(self, i: int, gourmet: int) -> None:
        self.i = i
        self.gourmet = gourmet


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people: list[Person] = []
current_gourmet = sys.maxsize
for i, a in enumerate(A):
    if a < current_gourmet:
        person = Person(i + 1, a)
        people.append(person)
        current_gourmet = a


def eater(deliciousness: int):
    ng = -1
    ok = len(people)
    # ok: 美食度が美味しさ以下である最小のインデックス
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if people[mid].gourmet <= deliciousness:
            ok = mid
        else:
            ng = mid

    if ok == len(people):
        return None
    else:
        return people[ok]


for b in B:
    eaten_person = eater(b)
    if eaten_person is None:
        print(-1)
    else:
        print(eaten_person.i)

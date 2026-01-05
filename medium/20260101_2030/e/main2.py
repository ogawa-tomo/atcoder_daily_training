class Person:
    def __init__(self, i: int, gourmet: int):
        self.i = i
        self.gourmet = gourmet


class Sushi:
    def __init__(self, i: int, deliciousness: int):
        self.i = i
        self.deliciousness = deliciousness
        self.eater: None | Person = None

    def __repr__(self):
        return str((self.i, self.deliciousness))


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people: list[Person] = []
for i, a in enumerate(A):
    person = Person(i + 1, a)
    people.append(person)

sushis: list[Sushi] = []
for i, b in enumerate(B):
    sushi = Sushi(i + 1, b)
    sushis.append(sushi)

sushis.sort(key=lambda sushi: sushi.deliciousness, reverse=True)
# print(sushis)
person_index = 0
for sushi in sushis:
    while True:
        if person_index >= N:
            break
        current_person = people[person_index]
        if current_person.gourmet <= sushi.deliciousness:
            sushi.eater = current_person
            break
        person_index += 1


sushis.sort(key=lambda sushi: sushi.i)
for sushi in sushis:
    if sushi.eater is None:
        print(-1)
    else:
        print(sushi.eater.i)

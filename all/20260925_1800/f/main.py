from fractions import Fraction


class Person:
    def __init__(self, i: int, a: int, b: int) -> None:
        self.i = i
        self.a = a
        self.b = b
        self.probability = Fraction(a, a + b)


N = int(input())

people: list[Person] = []
for i in range(N):
    a, b = map(int, input().split())
    person = Person(i + 1, a, b)
    people.append(person)

people.sort(key=lambda p: p.probability, reverse=True)
print(*[p.i for p in people])

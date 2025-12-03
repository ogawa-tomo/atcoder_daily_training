from fractions import Fraction


class Person:
    def __init__(self, i: int, a: int, b: int):
        self.i = i + 1
        self.a = a
        self.b = b
        self.rate = Fraction(a, a + b)

    def __lt__(self, other):
        return self.rate < other.rate

        # こうしなくても通る
        # if self.rate == other.rate:
        #     return self.i > other.i
        # else:
        #     return self.rate < other.rate

    def __repr__(self):
        return str(self.i)


N = int(input())

people: list[Person] = []
for i in range(N):
    a, b = map(int, input().split())
    person = Person(i, a, b)
    people.append(person)

people.sort(reverse=True)
print(*people)

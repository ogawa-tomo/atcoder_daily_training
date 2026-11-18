class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return str((self.last_name, self.first_name))


N = int(input())


people: list[Person] = []
for _ in range(N):
    s, t = input().split()
    person = Person(s, t)
    people.append(person)

for i in range(N):
    person = people[i]
    other_people = [*people[:i], *people[i + 1 :]]
    # print(person, other_people)
    other_names: set[str] = set()
    for p in other_people:
        other_names.add(p.first_name)
        other_names.add(p.last_name)
    if person.first_name in other_names and person.last_name in other_names:
        print("No")
        exit()

print("Yes")

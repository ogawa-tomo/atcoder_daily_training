class Person:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


N = int(input())
people: list[Person] = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append(Person(x, y))
S = list(input())

# min_r[y]: y座標で右に進む人のx座標の最小値
# max_l[y]: y座標で左に進む人のx座標の最大値
min_r: dict[int, int] = {}
max_l: dict[int, int] = {}

for i, s in enumerate(S):
    person = people[i]
    if s == "R":
        if person.y not in min_r:
            min_r[person.y] = person.x
        else:
            min_r[person.y] = min(min_r[person.y], person.x)
    else:
        if person.y not in max_l:
            max_l[person.y] = person.x
        else:
            max_l[person.y] = max(max_l[person.y], person.x)

    if person.y in min_r and person.y in max_l and min_r[person.y] < max_l[person.y]:
        print("Yes")
        exit()
print("No")

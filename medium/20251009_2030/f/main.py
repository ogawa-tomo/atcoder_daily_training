from itertools import permutations

N, M = map(int, input().split())


class City:
    def __init__(self, i: int):
        self.i = i
        self.roads: list[Road] = []

    def __repr__(self):
        return str(self.i)

    def to_cities(self):
        return [road.to_city for road in self.roads]


class Road:
    def __init__(self, to_city: City, length: int):
        self.to_city = to_city
        self.length = length


cities = [City(i) for i in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    from_city = cities[a]
    to_city = cities[b]
    road = Road(to_city, c)
    from_city.roads.append(Road(to_city, c))
    to_city.roads.append(Road(from_city, c))

answer = 0
for pattern in permutations(cities):
    length = 0
    # print(pattern)
    for i in range(N - 1):
        current_city = pattern[i]
        next_city = pattern[i + 1]
        can_go_next_city = False
        for road in current_city.roads:
            if road.to_city == next_city:
                length += road.length
                can_go_next_city = True
                break
        if not can_go_next_city:
            break
    answer = max(answer, length)

print(answer)

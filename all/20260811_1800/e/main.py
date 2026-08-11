from collections import defaultdict


class Dish:
    def __init__(self) -> None:
        self.ingredients: set[int] = set()


# dishes[i]: 食材iを使っている料理の集合
dishes: defaultdict[int, set[Dish]] = defaultdict(set)

N, M = map(int, input().split())
dish_list = [Dish() for _ in range(M)]
for i in range(M):
    dish = dish_list[i]
    row = list(map(int, input().split()))
    K = row[0]
    A = row[1:]
    for a in A:
        dish.ingredients.add(a)
        dishes[a].add(dish)

B = list(map(int, input().split()))

answer = 0
for b in B:
    dish_set = dishes[b]
    for dish in dish_set:
        if len(dish.ingredients) == 0:
            continue
        dish.ingredients.remove(b)
        if len(dish.ingredients) == 0:
            answer += 1
    print(answer)

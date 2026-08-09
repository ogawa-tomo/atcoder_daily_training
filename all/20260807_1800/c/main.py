N, M = map(int, input().split())


class Item:
    def __init__(self, price: int, functions: set[int]) -> None:
        self.price = price
        self.functions = functions

    def superior(self, other):
        return (self.price <= other.price and self.functions >= other.functions) and (
            self.price < other.price or self.functions > other.functions
        )


items: list[Item] = []
for _ in range(N):
    row = list(map(int, input().split()))
    p = row[0]
    c = row[1]
    f = set(row[2:])
    # print(p, c, f)
    item = Item(p, f)
    items.append(item)

for item1 in items:
    for item2 in items:
        if item1.superior(item2):
            print("Yes")
            exit()
print("No")

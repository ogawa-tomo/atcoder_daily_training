class Shop:
    def __init__(self, data: str) -> None:
        self.data = data

    # i番目の味を売っているか
    def sells(self, i: int):
        return self.data[i] == "o"


N, M = map(int, input().split())

shops: list[Shop] = []
for _ in range(N):
    s = input()
    shop = Shop(s)
    shops.append(shop)

answer = 100
for i in range(1 << N):
    # i: お店をまわるパターン
    # このパターンですべての味が手に入るか
    ok1 = True
    for j in range(M):
        # j番目の味が手に入るか
        ok2 = False
        for k in range(N):
            shop = shops[k]
            # k 番目のお店に行くパターンであり、その店でjを売っていればOK
            if i & (1 << k) and shop.sells(j):
                ok2 = True
                break
        if not ok2:
            ok1 = False
            break
    if ok1:
        answer = min(answer, i.bit_count())

print(answer)

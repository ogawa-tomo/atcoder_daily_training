class Medicine:
    def __init__(self, day_num: int, amount: int) -> None:
        self.day_num = day_num
        self.amount = amount


N, K = map(int, input().split())
medicines: list[Medicine] = []
for _ in range(N):
    a, b = map(int, input().split())
    medicine = Medicine(a, b)
    medicines.append(medicine)


# n日目に飲む数
def total_amount(n: int):
    total = 0
    for medicine in medicines:
        if n < medicine.day_num:
            total += medicine.amount
    return total


ng = -1
ok = 10**9 + 2
while (ok - ng) > 1:
    mid = (ok + ng) // 2
    if total_amount(mid) <= K:
        ok = mid
    else:
        ng = mid

print(ok + 1)

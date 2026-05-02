from collections import defaultdict


class Medicine:
    def __init__(self, day_num: int, amount: int) -> None:
        self.day_num = day_num
        self.amount = amount


N, K = map(int, input().split())
# minus[d]: d日目に減る薬の数
minus: defaultdict[int, int] = defaultdict(int)
days_set: set[int] = set()
days_set.add(0)
medicines: list[Medicine] = []
total_amount = 0
for _ in range(N):
    a, b = map(int, input().split())
    medicine = Medicine(a, b)
    medicines.append(medicine)
    total_amount += b
    minus[a] += b
    days_set.add(a)

# print(minus)
days_list = list(days_set)
days_list.sort()
# print(days_list)

# if total_amount <= K:
#     print(1)
#     exit()

for day in days_list:
    total_amount -= minus[day]
    if total_amount <= K:
        print(day + 1)
        exit()

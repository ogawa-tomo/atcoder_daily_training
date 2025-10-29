import heapq


class Number:
    def __init__(self, value: int):
        self.value = value
        self.before_value_num = 0
        self.after_numbers: list[Number] = []

    def __lt__(self, other):
        return self.value < other.value


N, M = map(int, input().split())

numbers = [Number(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    number_a = numbers[a]
    number_b = numbers[b]
    number_a.after_numbers.append(number_b)
    number_b.before_value_num += 1

settable_numbers: list[Number] = []
for number in numbers:
    if number.before_value_num == 0:
        heapq.heappush(settable_numbers, number)

answer_numbers: list[Number] = []
while settable_numbers:
    number = heapq.heappop(settable_numbers)
    for after_number in number.after_numbers:
        after_number.before_value_num -= 1
        if after_number.before_value_num == 0:
            heapq.heappush(settable_numbers, after_number)
    answer_numbers.append(number)

if len(answer_numbers) < N:
    print(-1)
else:
    print(" ".join([str(n.value + 1) for n in answer_numbers]))

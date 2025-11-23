K = int(input())


numbers: list[int] = []
for k in range(1 << 10):
    num_list: list[int] = []
    for d in range(10):
        if k & (1 << d):
            num_list.append(d)
    if len(num_list) == 0:
        continue
    if num_list == [0]:
        continue
    num_list.sort(reverse=True)
    numbers.append(int("".join([str(n) for n in num_list])))

numbers.sort()
# for number in numbers:
#     print(number)

print(numbers[K - 1])

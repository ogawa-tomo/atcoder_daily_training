K = int(input())


def next_number(number: int) -> int:
    if number <= 9:
        return number + 1
    num_list = list(map(int, list(str(number))))
    length = len(num_list)
    for k in range(length - 1, 0, -1):
        # k桁目について
        digit = num_list[k]
        prev_digit = num_list[k - 1]
        if prev_digit > digit + 1:
            digit += 1
            new_num_list = [
                *num_list[:k],
                digit,
                *reversed(list(range(length - k - 1))),
            ]
            return int("".join([str(n) for n in new_num_list]))
    if num_list[0] < 9:
        new_num_list = [num_list[0] + 1, *reversed(list(range(length - 1)))]
        return int("".join([str(n) for n in new_num_list]))

    return int("".join([str(n) for n in reversed(list(range(length + 1)))]))


number = 1
for i in range(K - 1):
    # print(number)
    number = next_number(number)

print(number)

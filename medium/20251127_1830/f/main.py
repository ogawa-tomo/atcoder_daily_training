N = int(input())

binN = bin(N)
one_zero_list = list(map(int, list(binN[2:])))
one_zero_list.reverse()
one_zero_list_length = len(one_zero_list)
one_digits: list[int] = []
for i in range(one_zero_list_length):
    if one_zero_list[i]:
        one_digits.append(i)
one_digits_length = len(one_digits)
# one_zero_list.reverse()
# print(one_digits)

# print(one_zero_list)
# print(one_digits)

answers: list[int] = []
for i in range(1 << one_digits_length):
    num: list[str] = []
    one_digit = 0
    for d in range(one_zero_list_length):
        # d桁目
        if one_zero_list[d]:
            if i >> one_digit & 1:
                num.append("1")
            else:
                num.append("0")
            one_digit += 1
        else:
            num.append("0")
    num.reverse()
    # print(num)
    print(int("".join(num), 2))

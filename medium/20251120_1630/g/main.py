import sys

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

answers: list[list[int]] = []


def func(current_list: list[int]):
    length = len(current_list)

    if length == N:
        answers.append(current_list)
        return

    if length == 0:
        last_num = -9
    else:
        last_num = current_list[length - 1]

    next_num_min = last_num + 10
    next_num_max = M - (10 * (N - length - 1))
    for next_num in range(next_num_min, next_num_max + 1):
        next_list = [*current_list, next_num]
        func(next_list)


func([])

print(len(answers))
for answer in answers:
    print(*answer)

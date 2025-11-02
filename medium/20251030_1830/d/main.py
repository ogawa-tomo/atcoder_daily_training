L, R = map(int, input().split())
S = list(input())

first_part = S[: L - 1]
second_part = S[L - 1 : R]
third_part = S[R:]
# second_part.reverse()
# print(first_part, second_part, third_part)
print("".join([*first_part, *reversed(second_part), *third_part]))

N = int(input())
S = list(map(int, list(input())))
S.sort()


# 数字iがSの並べ替えで表現できるかを判定する
def can_express(i: int):
    i_list = list(map(int, list(str(i))))
    # print(i_list)
    if len(i_list) < N:
        for _ in range(N - len(i_list)):
            i_list.append(0)
    # print(i_list)
    i_list.sort()
    return i_list == S


# print(math.factorial(13))
# can_express(132)
answer = 0
for i in range(1000000000):
    squared = i**2
    if squared > 10**N:
        break
    if can_express(squared):
        answer += 1
print(answer)

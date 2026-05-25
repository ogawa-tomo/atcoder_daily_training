from collections import defaultdict

N = int(input())
S = list(map(int, list(input())))


# 数字iがSの並べ替えで表現できるかを判定する
def can_express(i: int):
    # s_dict[s]: 数字sが残り使える回数
    s_dict: defaultdict[int, int] = defaultdict(int)
    for s in S:
        s_dict[s] += 1
    # print(s_dict)
    i_list = list(map(int, list(str(i))))
    # print(i_list)
    if len(i_list) < N:
        i_list.reverse()
        for _ in range(N - len(i_list)):
            i_list.append(0)
        i_list.reverse()
    # print(i_list)
    for s in i_list:
        if s_dict[s] == 0:
            return False
        s_dict[s] -= 1
    return True


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

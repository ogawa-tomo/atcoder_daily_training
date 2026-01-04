from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(list(set(A)), reverse=True)
# print(A)
# print(sorted_A)


def num_of_larger_than(a: int):
    ok = -1
    ng = len(sorted_A)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        # print(ng, ok, mid)
        if sorted_A[mid] > a:
            ok = mid
        else:
            ng = mid
    return ok + 1


# answers[k]: Aに含まれる整数のうちA_iより大きいものがちょうどk種類であるようなiの個数
answers: defaultdict[int, int] = defaultdict(int)
for a in A:
    num = num_of_larger_than(a)
    answers[num] += 1
# print(answers)
for i in range(N):
    print(answers[i])

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


# num_of_larger_than_A[i]: A[i]より大きいものの数
num_of_larger_than_A: defaultdict[int, int] = defaultdict(int)
for i in range(N):
    num_of_larger_than_A[i] = num_of_larger_than(A[i])

# print(num_of_larger_than_A)

# answers[k]: Aiより大きいAがk種類であるようなAの個数
answers: defaultdict[int, int] = defaultdict(int)
for i, a in enumerate(A):
    num = num_of_larger_than_A[i]
    answers[num] += 1
# print(answers)
for i in range(N):
    print(answers[i])

from collections import defaultdict

N = int(input())
A_ = list(map(int, input().split()))
A = [a - 1 for a in A_]

# index[a]:数字aのインデックス
index: defaultdict[int, int] = defaultdict(int)
for i in range(N):
    a = A[i]
    index[a] = i

answers: list[tuple[int, int]] = []
for i in range(N):
    a = A[i]
    if a != i:
        to_index = index[i]
        to_a = A[to_index]
        # print(i + 1, to_index + 1)
        answers.append((i + 1, to_index + 1))
        A[i] = i
        A[to_index] = a
        index[i] = i
        index[a] = to_index

print(len(answers))
for answer in answers:
    print(*answer)

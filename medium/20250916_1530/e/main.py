N = int(input())
A = list(map(int, input().split()))

n_dict: dict[int, int] = {}
for i in range(N):
    n_dict[i + 1] = 0
# print(n_dict)
answers: list[int] = []
for a in A:
    n_dict[a] += 1
    if n_dict[a] == 2:
        answers.append(a)

print(" ".join([str(a) for a in answers]))

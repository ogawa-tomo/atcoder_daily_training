N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_a = max(A)
max_indice: list[int] = []
for i in range(N):
    if A[i] == max_a:
        max_indice.append(i)

for index in max_indice:
    if index + 1 in B:
        print("Yes")
        exit()

print("No")

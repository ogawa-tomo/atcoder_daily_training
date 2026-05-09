N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()
# print(C)
a_set = set(A)
b_set = set(B)
a_answer: list[int] = []
b_answer: list[int] = []

for i, c in enumerate(C):
    if c in a_set:
        a_answer.append(i + 1)
    else:
        b_answer.append(i + 1)

print(*a_answer)
print(*b_answer)

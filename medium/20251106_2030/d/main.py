N, L, R = map(int, input().split())
A = list(map(int, input().split()))

answer: list[int] = []
for a in A:
    if a <= L:
        answer.append(L)
    elif R <= a:
        answer.append(R)
    else:
        answer.append(a)
print(*answer)

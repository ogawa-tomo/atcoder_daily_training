N = int(input())
A = [0, *list(map(int, input().split()))]

eq_num = 0
answer = 0
for i in range(1, N + 1):
    a = A[i]
    if a == i:
        eq_num += 1
    else:
        if a > i and A[a] == i:
            answer += 1
answer += (eq_num * (eq_num - 1)) // 2
print(answer)

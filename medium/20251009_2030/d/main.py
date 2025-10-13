T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd_count = 0
    for a in A:
        if a % 2 == 1:
            odd_count += 1
    print(odd_count)

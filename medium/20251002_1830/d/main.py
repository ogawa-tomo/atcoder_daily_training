N, T, P = map(int, input().split())
L = list(map(int, input().split()))

for d in range(101):
    count = 0
    for l in L:
        if l + d >= T:
            count += 1
    if count >= P:
        print(d)
        exit()

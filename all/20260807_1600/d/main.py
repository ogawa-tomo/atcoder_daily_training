N, M = map(int, input().split())

juices = set(range(1, M + 1))
for _ in range(N):
    l = int(input())
    x = list(map(int, input().split()))
    found = False
    for xx in x:
        if xx in juices:
            print(xx)
            juices.remove(xx)
            found = True
            break
    if not found:
        print(0)

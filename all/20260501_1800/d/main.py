N, M = map(int, input().split())
selected: set[int] = set()
for _ in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    drunk = False
    for x in X:
        if x not in selected:
            print(x)
            selected.add(x)
            drunk = True
            break
    if not drunk:
        print(0)

N = int(input())

usables: set[int] = set(list(range(1, 2 * N + 2)))
while True:
    print(usables.pop(), flush=True)

    t = int(input())
    if t == 0:
        exit()
    usables.remove(t)

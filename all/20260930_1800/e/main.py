N = int(input())

slots: list[list[int]] = []
for _ in range(N):
    slot = list(map(int, list(input())))
    slots.append(slot)

# print(slots)
answer = 10**9
for i in range(10):
    t_set: set[int] = set()
    for slot in slots:
        for t in range(10):
            s = slot[t]
            if s == i:
                add_t = t
                while True:
                    if add_t not in t_set:
                        t_set.add(add_t)
                        break
                    add_t += 10
                break
    answer = min(answer, max(t_set))

print(answer)

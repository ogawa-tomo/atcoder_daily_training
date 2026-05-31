from itertools import permutations

N, M = map(int, input().split())

ab_set: set[tuple[int, int]] = set()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab_set.add((a, b))
    ab_set.add((b, a))

cd_set: set[tuple[int, int]] = set()
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    cd_set.add((c, d))
    cd_set.add((d, c))

# print(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
for p in permutations(range(N)):
    # print(p)
    new_cd_set: set[tuple[int, int]] = set()
    for cd in cd_set:
        new_c = p[cd[0]]
        new_d = p[cd[1]]
        new_cd_set.add((new_c, new_d))
    if ab_set == new_cd_set:
        print("Yes")
        exit()
print("No")

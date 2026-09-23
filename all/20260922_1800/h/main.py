# TLE
N, K = map(int, input().split())
P = [0]
P.extend(list(map(int, input().split())))
# for i in range(N):
#     P[i] -= 1
Plist: list[list[int]] = [P]

mod = 1
while True:
    print(mod)
    beforeP = Plist[-1]
    newP = [0] * (N + 1)
    for i in range(1, N + 1):
        newP[i] = beforeP[beforeP[i]]
    if newP == P:
        break
    mod += 1
    Plist.append(newP)
# print(mod)
# for p in Plist:
#     print(p)

answer = Plist[K % mod]
print(*answer[1:])

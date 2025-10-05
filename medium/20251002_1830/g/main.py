N = int(input())
A = list(map(int, input().split()))

max_num = 2 * 10**5
# max_num = 10
# emerge[num]: numが出現した回数
emerge: list[int] = [0] * (max_num + 1)
for a in A:
    emerge[a] += 1

answer = 0
for p in range(1, max_num + 1):
    for q in range(1, max_num // p + 1):
        # r/p == q となる組
        r = p * q
        answer += emerge[p] * emerge[q] * emerge[r]

print(answer)

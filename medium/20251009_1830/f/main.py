N, K = map(int, input().split())
R = list(map(int, input().split()))

for i in range(5**N):
    answer: list[int] = []
    # 右からk桁目の数
    for k in range(N):
        digit = (i // (5**k)) % 5 + 1
        answer.append(digit)
    answer.reverse()
    ok = True
    for i in range(N):
        a = answer[i]
        r = R[i]
        if a > r:
            ok = False
            break
    if ok and sum(answer) % K == 0:
        print(" ".join([str(a) for a in answer]))

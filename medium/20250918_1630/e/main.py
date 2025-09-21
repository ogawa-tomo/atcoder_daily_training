N = int(input())
A = list(map(int, input().split()))

# last_emerge[num]: numが最後に現れたインデックス
last_emerge: dict[int, int] = {}
B: list[int] = []

for i in range(N):
    a = A[i]
    if a in last_emerge:
        B.append(last_emerge[a] + 1)
    else:
        B.append(-1)
    last_emerge[a] = i

print(" ".join([str(b) for b in B]))

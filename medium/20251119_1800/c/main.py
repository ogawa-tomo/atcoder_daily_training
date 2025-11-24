N = int(input())
A = list(map(int, input().split()))

angle = 0
cut = [0]
for a in A:
    angle += a
    angle %= 360
    cut.append(angle)

cut.append(360)
cut = list(set(cut))
cut.sort()
length = len(cut)

answer = 0
for i in range(length - 1):
    angle = cut[i + 1] - cut[i]
    answer = max(answer, angle)

print(answer)

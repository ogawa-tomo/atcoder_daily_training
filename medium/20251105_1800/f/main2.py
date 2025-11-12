N = int(input())
S = list(input())

answer = 1
for i in range(N):
    s = S[i]
    if s != "/":
        continue
    count = 1
    while True:
        if i - count < 0 or N <= i + count:
            break
        l = S[i - count]
        r = S[i + count]
        if l == "1" and r == "2":
            answer = max(answer, count * 2 + 1)
            count += 1
            continue
        else:
            break

print(answer)

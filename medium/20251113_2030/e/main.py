N, K = map(int, input().split())

S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

answer = 0
for i in range(1 << N):
    string = ""
    for k in range(N):
        if i >> k & 1:
            string += S[k]
    string_list = list(string)
    K_count = 0
    for alphabet in "abcdefghijklmnopqrstuvwxyz":
        if string_list.count(alphabet) == K:
            K_count += 1
    answer = max(answer, K_count)

print(answer)

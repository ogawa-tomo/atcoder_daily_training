N = int(input())

answer = 1
for i in range(N - 1):
    answer += sum(list(map(int, list(str(answer)))))
    # print(i, answer)
print(answer)

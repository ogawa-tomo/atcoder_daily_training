N = int(input())

answer = 0
while True:
    if 2**answer > N:
        print(answer - 1)
        exit()
    answer += 1

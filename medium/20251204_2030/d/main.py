N = int(input())

logged_in = False

answer = 0
for _ in range(N):
    s = input()
    if s == "login":
        logged_in = True
    elif s == "logout":
        logged_in = False
    elif s == "public":
        pass
    elif s == "private":
        if not logged_in:
            answer += 1

print(answer)

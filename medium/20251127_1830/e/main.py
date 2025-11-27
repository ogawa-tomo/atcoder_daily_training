N = int(input())

highest_head = 0
body = 0
for _ in range(N):
    a, b = map(int, input().split())
    body += a
    highest_head = max(highest_head, b - a)

print(body + highest_head)

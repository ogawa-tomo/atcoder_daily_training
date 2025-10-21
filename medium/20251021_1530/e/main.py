N = int(input())

shoulder_sum = 0
longest_head = 0
for _ in range(N):
    a, b = map(int, input().split())
    shoulder_sum += a
    longest_head = max(longest_head, b - a)

print(shoulder_sum + longest_head)

N = int(input())

left = 0
right = N - 1
while right - left > 1:
    mid = (left + right) // 2
    print("?", mid + 1, flush=True)
    ans = int(input())
    if ans == 0:
        left = mid
    else:
        right = mid

print("!", left + 1, flush=True)

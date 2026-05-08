N = int(input())
nums: set[int] = set()
for i in range(1, 2 * N + 2):
    nums.add(i)
# print(nums)
# nums.remove(3)
# print(nums)
while True:
    # print(nums)
    print(nums.pop(), flush=True)
    n = int(input())
    if n == 0:
        exit()
    else:
        nums.remove(n)

from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())

for k in range(K):
    # X = round(X, -k - 1)
    # print(X)
    X = Decimal(str(X)).quantize(Decimal(f"1E{k + 1}"), ROUND_HALF_UP)
    # print(int(X))
print(int(X))

# nums = list(map(int, list(str(X))))
# print(nums)
# nums.reverse()

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    # i日目

    b = B[i]  # 必要なパスタの長さ
    if b not in A:
        print("No")
        exit()

    index = A.index(b)
    A.pop(index)

# print(A)
print("Yes")

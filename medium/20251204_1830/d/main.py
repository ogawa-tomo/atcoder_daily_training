A_, B_ = map(int, input().split())

A = list(map(int, list(str(A_))))
B = list(map(int, list(str(B_))))

# print(A, B)
A.reverse()
B.reverse()
length = min(len(A), len(B))

for d in range(length):
    a = A[d]
    b = B[d]
    if a + b >= 10:
        print("Hard")
        exit()

print("Easy")

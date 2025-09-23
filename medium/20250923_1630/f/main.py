S = list(map(int, list(input())))
N = len(S)
S.reverse()
# print(S)

b_counter = 0
for i in range(N):
    s = S[i]
    b_counter += (s - b_counter) % 10
    # b_counter %= 10
print(b_counter + N)

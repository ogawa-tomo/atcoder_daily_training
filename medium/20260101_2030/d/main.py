P = list(map(int, input().split()))

# print(ord("a")) # 97
answer = ""
for p in P:
    answer += chr(96 + p)

print(answer)

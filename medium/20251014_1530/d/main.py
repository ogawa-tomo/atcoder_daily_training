N = int(input())

S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

S.sort(key=lambda x: len(x))
print("".join(S))

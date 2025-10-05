N = int(input())

suits = ["H", "D", "C", "S"]
nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

emerged: list[str] = []
for _ in range(N):
    s = input()
    if s[0] not in suits:
        print("No")
        exit()
    if s[1] not in nums:
        print("No")
        exit()
    if s in emerged:
        print("No")
        exit()
    emerged.append(s)
print("Yes")

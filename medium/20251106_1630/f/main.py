from itertools import permutations
import sys

M = int(input())

S: list[list[int]] = []

S.append(list(map(int, list(input()))))
S.append(list(map(int, list(input()))))
S.append(list(map(int, list(input()))))
# print(S)

answer = sys.maxsize
for s in range(10):
    # sの存在チェック
    if s not in S[0] or s not in S[1] or s not in S[2]:
        continue
    for slot_perm in permutations([0, 1, 2]):
        # スロットをこの順番でsで揃えるために必要な秒数
        second = 0
        for slot_num in slot_perm:
            slot = S[slot_num]
            for sec in range(second, second + M):
                slot_value = slot[sec % M]
                if slot_value == s:
                    break
            second = sec + 1
        second -= 1
        answer = min(answer, second)

if answer < sys.maxsize:
    print(answer)
else:
    print(-1)

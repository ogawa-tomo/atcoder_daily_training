S = list(input())

N = len(S)

# 残る文字のインデックス
answer_indice: list[int] = []
i = 0
while i < N:
    if i >= N - 2 or S[i] + S[i + 1] + S[i + 2] != "ABC":
        # iは採用して大丈夫
        answer_indice.append(i)
        i += 1
        continue
    # iから始まるのがABCだったとき
    i += 3
    # 既存の答えと合わせてABCだったら取り除く
    while True:
        if i >= N:
            break
        answer_len = len(answer_indice)
        # 既存の答えの末尾がA、続きがBCだったとき
        if (
            answer_len > 0
            and S[answer_indice[answer_len - 1]] == "A"
            and S[i] == "B"
            and i + 1 < N
            and S[i + 1] == "C"
        ):
            answer_indice.pop()
            i += 2
            continue
        if (
            answer_len > 1
            and S[answer_indice[answer_len - 2]] == "A"
            and S[answer_indice[answer_len - 1]] == "B"
            and S[i] == "C"
        ):
            answer_indice.pop()
            answer_indice.pop()
            i += 1
            continue
        break

answer: list[str] = []
for i in answer_indice:
    answer.append(S[i])
print("".join(answer))

N = int(input())

bin_N_length = len(bin(N)[2:])
answers: list[int] = [0]
for i in range(bin_N_length):
    if N & 1 << i:
        added_answers: list[int] = []
        for answer in answers:
            added_answers.append(answer | 1 << i)
        answers.extend(added_answers)

for answer in answers:
    print(answer)

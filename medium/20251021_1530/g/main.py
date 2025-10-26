# TLE
N = int(input())
S = list(input())

answer = [0]
current_index = 0
for i in range(N):
    s = S[i]
    if s == "L":
        # answerのcurrent_indexの左にi + 1を差し込む
        left = answer[:current_index]
        right = answer[current_index:]
    elif s == "R":
        left = answer[: current_index + 1]
        right = answer[current_index + 1 :]
    # extendにはO(N)かかるのでTLE
    left.extend([i + 1])
    left.extend(right)
    answer = left
    if s == "R":
        current_index += 1

print(" ".join([str(a) for a in answer]))

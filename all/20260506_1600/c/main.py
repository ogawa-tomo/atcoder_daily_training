N, S, M, L = map(int, input().split())
answer = 10**9
for s_num in range(20):
    for m_num in range(14):
        for l_num in range(10):
            if 6 * s_num + 8 * m_num + 12 * l_num >= N:
                answer = min(answer, S * s_num + M * m_num + L * l_num)

print(answer)

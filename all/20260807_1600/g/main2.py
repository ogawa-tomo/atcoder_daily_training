from itertools import combinations
import sys

N, M = map(int, input().split())
edges: set[tuple[int, int]] = set()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a < b:
        edges.add((a, b))
    else:
        edges.add((b, a))

# print(edges)

all_edges: set[tuple[int, int]] = set()
for i in range(N - 1):
    for j in range(i + 1, N):
        all_edges.add((i, j))
# print(all_edges)


answer = sys.maxsize
for edge_combination in combinations(all_edges, N):
    edge_num_list = [0] * N
    for u, v in edge_combination:
        edge_num_list[u] += 1
        edge_num_list[v] += 1
    all_2 = True
    for num in edge_num_list:
        if num != 2:
            all_2 = False
            break
    if all_2:
        current_answer = 0
        edge_combination_set = set(edge_combination)
        current_answer += len(edges - edge_combination_set)
        current_answer += len(edge_combination_set - edges)
        answer = min(answer, current_answer)

print(answer)

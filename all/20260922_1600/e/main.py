import sys
from itertools import permutations

N = int(input())
Mg = int(input())
g_links_data: list[tuple[int, int]] = []
for _ in range(Mg):
    u, v = map(int, input().split())
    g_links_data.append((u - 1, v - 1))
Mh = int(input())
h_links: list[tuple[int, int]] = []
for _ in range(Mh):
    a, b = map(int, input().split())
    h_links.append((a - 1, b - 1))
A: list[list[int]] = []
for i in range(N - 1):
    a = list(map(int, input().split()))
    row = [0] * (i + 1)
    row.extend(a)
    A.append(row)

# print(A)
#
# print(2**28)
# print(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)

answer = sys.maxsize
h_nodes = list(range(N))
for g_nodes in permutations(range(N)):
    # print(g_nodes)
    g_links: list[tuple[int, int]] = []
    for g_link_data in g_links_data:
        # print(g_link_data)
        min_i = min(g_nodes[g_link_data[0]], g_nodes[g_link_data[1]])
        max_i = max(g_nodes[g_link_data[0]], g_nodes[g_link_data[1]])
        g_links.append((min_i, max_i))

    cost = 0
    # print(g_links, h_links)
    for g_link in g_links:
        if g_link not in h_links:
            cost += A[g_link[0]][g_link[1]]
    for h_link in h_links:
        if h_link not in g_links:
            cost += A[h_link[0]][h_link[1]]
    # print(cost)

    answer = min(answer, cost)

print(answer)

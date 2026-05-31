# なぜかWA...
from itertools import permutations

N, M = map(int, input().split())


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []

    @property
    def to_nodes_id_set(self):
        return set([to_node.i for to_node in self.to_nodes])


nodes1 = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes1[a].to_nodes.append(nodes1[b])
    nodes1[b].to_nodes.append(nodes1[a])

nodes2 = [Node(i) for i in range(N)]
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    nodes2[c].to_nodes.append(nodes2[d])
    nodes2[d].to_nodes.append(nodes2[c])

# print(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
for p in permutations(range(N)):
    # print(p)
    matched = True
    for i in range(N):
        node1 = nodes1[i]
        node2 = nodes2[p[i]]
        node2_to_id_set = set()
        for node2_to_node in node2.to_nodes:
            node2_to_id_set.add(p[node2_to_node.i])
        if node1.to_nodes_id_set != node2_to_id_set:
            matched = False
            break
    if matched:
        print("Yes")
        exit()

print("No")

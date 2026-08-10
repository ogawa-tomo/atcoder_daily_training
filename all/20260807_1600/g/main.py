import sys
from itertools import permutations


class Node:
    def __init__(self, i) -> None:
        self.i = i
        self.to_nodes: set[Node] = set()

    def __repr__(self) -> str:
        return str(self.i)


N, M = map(int, input().split())
nodes = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.to_nodes.add(node_b)
    node_b.to_nodes.add(node_a)


def operation_num(order: list[int]):
    n = len(order)
    num = 0
    for i in range(n):
        current_node = nodes[order[i]]
        next_node = nodes[order[(i + 1) % n]]
        before_node = nodes[order[(i - 1) % n]]
        target_nodes = set((next_node, before_node))
        num += len(target_nodes - current_node.to_nodes)
        num += len(current_node.to_nodes - target_nodes)
    return num


answer = sys.maxsize
for perm in permutations(range(N)):
    answer = min(answer, operation_num(list(perm)) // 2)
    if N < 6:
        continue

    for split in range(3, 6):
        p1 = list(perm[:split])
        # print(p1)
        p2 = list(perm[split:])
        if len(p1) < 3 or len(p2) < 3:
            continue
        current_answer = operation_num(p1) + operation_num(p2)
        current_answer //= 2
        answer = min(answer, current_answer)

print(answer)

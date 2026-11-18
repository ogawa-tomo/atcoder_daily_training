from collections import deque
import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_links: list[Link] = []
        self.visited = False
        self.distance_from: dict[Node, int] = dict()

    def __repr__(self) -> str:
        return str(self.i)


class Link:
    def __init__(self, distance: int, to_node: Node) -> None:
        self.distance = distance
        self.to_node = to_node


N = int(input())

distance_list: list[list[int]] = []
for _ in range(N - 1):
    A = list(map(int, input().split()))
    distance_list.append(A)


def get_distance(i: int, j: int):
    if i == j:
        return 0
    left = min(i, j)
    right = max(i, j)

    return distance_list[left][right - left - 1]


nodes = [Node(i) for i in range(N)]

root = nodes[0]
for i in range(1, N):
    node = nodes[i]
    root_distance = get_distance(0, i)
    ancestors: list[Node] = []
    for j in range(1, N):
        if i == j:
            continue
        root_through_j_distance = get_distance(0, j) + get_distance(j, i)
        if root_distance == root_through_j_distance:
            ancestors.append(nodes[j])

    if ancestors:
        min_distance = sys.maxsize
        parent_candidates_num = 0
        parent = ancestors[0]
        for a in ancestors:
            a_distance = get_distance(a.i, i)
            if a_distance < min_distance:
                min_distance = a_distance
                parent_candidates_num = 0
                parent = a
            elif a_distance == min_distance:
                parent_candidates_num += 1
        if parent_candidates_num > 1:
            print("No")
            exit()
        distance = min_distance
    else:
        parent = root
        distance = root_distance
    node.to_links.append(Link(distance, parent))
    parent.to_links.append(Link(distance, node))


def dfs(node: Node, start: Node, current_distance: int):
    node.visited = True
    node.distance_from[start] = current_distance
    for to_link in node.to_links:
        to_node = to_link.to_node
        # if not to_node.visited:
        if start not in to_node.distance_from:
            dfs(to_node, start, current_distance + to_link.distance)


def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.distance_from[start_node] = 0
    while d:
        node = d.popleft()
        distance = node.distance_from[start_node]
        for to_link in node.to_links:
            to_node = to_link.to_node
            if start_node not in to_node.distance_from:
                d.append(to_node)
                to_node.distance_from[start_node] = distance + to_link.distance


for node in nodes:
    # dfsだとTLEになっちゃった
    # for n in nodes:
    #     n.visited = False
    # dfs(node, node, 0)
    bfs(node)


for i in range(N - 1):
    for j in range(i + 1, N):
        from_node = nodes[i]
        to_node = nodes[j]

        if get_distance(i, j) != to_node.distance_from[from_node]:
            print("No")
            exit()

print("Yes")

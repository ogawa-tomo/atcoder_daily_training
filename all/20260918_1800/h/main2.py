# わかんなかった
import heapq
import sys

max_joy = sys.maxsize


class Node:
    def __init__(self, height: int) -> None:
        self.height = height
        self.links: list[Link] = []
        # self.height_plus_joy = max_joy
        self.finalized = False
        self.cost = sys.maxsize

    @property
    def joy(self):
        return self.height - self.cost

    def __repr__(self) -> str:
        return str(self.cost)


class Link:
    def __init__(self, to_node: Node, cost: int) -> None:
        self.to_node = to_node
        self.cost = cost


# キューには同じノードが追加されることがある。
# キューに追加済みのノードに対してdistanceを操作すると、キューが正常に動作しない。
# したがって、キューに追加するための専用のクラスを用意する。
class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.cost = node.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return str(self.cost)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.cost = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for link in node.links:
            cost = node.cost + link.cost
            if cost < link.to_node.cost:
                link.to_node.cost = cost
                heapq.heappush(q, QueueObject(link.to_node))


N, M = map(int, input().split())

nodes: list[Node] = []
H = list(map(int, input().split()))
for h in H:
    nodes.append(Node(h))

for _ in range(M):
    u, v = map(int, input().split())
    node_u = nodes[u - 1]
    node_v = nodes[v - 1]
    if node_u.height > node_v.height:
        height_diff = node_u.height - node_v.height
        node_u.links.append(Link(node_v, 0))  # 下がるのでコスト0
        node_v.links.append(Link(node_u, height_diff))  # 上がるので標高差コスト
    else:
        height_diff = node_v.height - node_u.height
        node_u.links.append(Link(node_v, height_diff))  # 上がるので標高差コスト
        node_v.links.append(Link(node_u, 0))  # 下がるのでコスト0

dijkstra(nodes[0])

answer_node = nodes[0]
# answer = 0
for node in nodes:
    if node.height + node.cost < answer_node.height + answer_node.cost:
        answer_node = node

# print(nodes)
# print(answer)
print(answer_node.joy)

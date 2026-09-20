# AC
import heapq
import sys


class Node:
    def __init__(self, height: int) -> None:
        self.height = height
        self.to_nodes: list[Node] = []
        self.finalized = False
        self.total_up = 0
        self.total_down = 0
        self.total_updown = sys.maxsize

    @property
    def joy(self):
        return self.total_down - self.total_up * 2

    def __repr__(self) -> str:
        return str(
            {
                "total_up": self.total_up,
                "total_down": self.total_down,
                "total_updown": self.total_updown,
            }
        )


# キューには同じノードが追加されることがある。
# キューに追加済みのノードに対してdistanceを操作すると、キューが正常に動作しない。
# したがって、キューに追加するための専用のクラスを用意する。
class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.total_updown = node.total_updown

    def __lt__(self, other):
        return self.total_updown < other.total_updown

    def __repr__(self):
        return str(self.total_updown)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.total_updown = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for to_node in node.to_nodes:
            total_updown = node.total_updown + abs(to_node.height - node.height)
            if total_updown < to_node.total_updown:
                to_node.total_updown = total_updown
                if to_node.height > node.height:
                    to_node.total_up = node.total_up + to_node.height - node.height
                    to_node.total_down = node.total_down
                else:
                    to_node.total_down = node.total_down + node.height - to_node.height
                    to_node.total_up = node.total_up
                heapq.heappush(q, QueueObject(to_node))


N, M = map(int, input().split())

nodes: list[Node] = []
H = list(map(int, input().split()))
for h in H:
    nodes.append(Node(h))

for _ in range(M):
    u, v = map(int, input().split())
    node_u = nodes[u - 1]
    node_v = nodes[v - 1]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)

dijkstra(nodes[0])

answer = 0
for node in nodes:
    answer = max(answer, node.joy)

# print(nodes)
print(answer)

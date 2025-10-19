X = list(input())
N = int(input())

d: dict[str, int] = {}
for i, x in enumerate(X):
    d[x] = i


class String:
    def __init__(self, value: str):
        self.value = value

    def __lt__(self, other):
        for i in range(min(len(self.value), len(other.value))):
            self_value = self.value[i]
            other_value = other.value[i]
            if self_value != other_value:
                return d[self_value] < d[other_value]
        return len(self.value) < len(other.value)


S: list[String] = []
for _ in range(N):
    s_ = input()
    S.append(String(s_))
S.sort()
for s in S:
    print(s.value)

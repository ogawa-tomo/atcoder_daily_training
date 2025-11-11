N = int(input())
A = list(map(int, input().split()))


class Number:
    def __init__(self, index: int, value: int):
        self.index = index
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


numbers: list[Number] = []
for i in range(N):
    a = A[i]
    numbers.append(Number(i, a))
numbers.sort(reverse=True)
print(numbers[1].index + 1)

import sys

N = int(input())
A = list(map(int, input().split()))

length = 10**6 + 1
# length = 10


class Data:
    def __init__(self) -> None:
        self.last_emerged_index: int | None = None


# data_list[num]: numが出た回数や場所に関する情報
data_list = [Data() for _ in range(length)]

inf = sys.maxsize

answer = inf
for i in range(N):
    a = A[i]
    data = data_list[a]
    if data.last_emerged_index is None:
        data.last_emerged_index = i
    else:
        answer = min(answer, i - data.last_emerged_index + 1)
        data.last_emerged_index = i

if answer == inf:
    print(-1)
else:
    print(answer)

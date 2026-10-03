class Data:
    def __init__(self) -> None:
        # self.block_emerged_num = 0 # 固まり単位
        self.total_emerged_num = 0  # 全部
        self.last_emerged_index = 0
        self.last_repeat_num = 0
        self.total = 0
        self.last_total = 0

    def __repr__(self) -> str:
        return str(
            {
                "total_emerged_num": self.total_emerged_num,
                "last_emerged_index": self.last_emerged_index,
                "last_repeat_num": self.last_repeat_num,
                "total": self.total,
            }
        )


N = int(input())
A = list(map(int, input().split()))

# d[n]: 数nのデータ
d: dict[int, Data] = {}
i = 0
while i <= N - 1:
    a = A[i]
    repeat = 1
    while i < N - 1 and A[i + 1] == a:
        i += 1
        repeat += 1

    if a not in d:
        data = Data()
        data.last_repeat_num = repeat
        data.last_emerged_index = i
        data.total_emerged_num = repeat
        d[a] = data
    else:
        data = d[a]
        repeat_start_index = i - repeat + 1
        sanded_num = repeat_start_index - data.last_emerged_index - 1
        current_total = (
            data.last_total // data.last_repeat_num
        ) * repeat + repeat * sanded_num * data.total_emerged_num
        data.total += current_total
        data.last_total = current_total

        data.total_emerged_num += repeat
        data.last_repeat_num = repeat
        data.last_emerged_index = i

    i += 1

answer = 0
for data in d.values():
    answer += data.total

print(answer)

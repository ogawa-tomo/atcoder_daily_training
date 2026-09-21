N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())


class Step:
    def __init__(self) -> None:
        self.mochi = False
        self.reach = False

    @property
    def can_reach(self):
        return not self.mochi


steps: list[Step] = []
for _ in range(10**6):
    steps.append(Step())

for b in B:
    steps[b].mochi = True

steps[0].reach = True
for i in range(X + 1):
    step = steps[i]
    if not step.reach:
        continue
    for a in A:
        to_step = steps[i + a]
        if to_step.can_reach:
            to_step.reach = True
            if i + a == X:
                print("Yes")
                exit()

print("No")

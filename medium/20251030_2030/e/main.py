import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Skill:
    def __init__(self, i: int):
        self.i = i
        self.to_skills: list[Skill] = []
        self.acquired = False


N = int(input())
skills = [Skill(i) for i in range(N)]
first_skills: list[Skill] = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    skill = skills[i]
    if a == -1 and b == -1:
        first_skills.append(skill)
        continue
    from_skill_a = skills[a]
    from_skill_b = skills[b]
    from_skill_a.to_skills.append(skill)
    from_skill_b.to_skills.append(skill)


def dfs(skill: Skill):
    skill.acquired = True
    for to_skill in skill.to_skills:
        if not to_skill.acquired:
            to_skill.acquired = True
            dfs(to_skill)


for first_skill in first_skills:
    dfs(first_skill)

answer = 0
for skill in skills:
    if skill.acquired:
        answer += 1
print(answer)

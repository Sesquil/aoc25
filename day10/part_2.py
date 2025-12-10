import re
import pulp

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"\[([.#]*)\](( \(\d+(,\d+)*\))+) \{(\d+(,\d+)*)\}")

res = 0
for p_id, line in enumerate(lines):
    match = regexp.match(line)
    #lights = match[1]
    buttons = [tuple(int(x) for x in s[1:-1].split(",")) for s in match[2].split()]
    joltage = tuple(int(x) for x in match[match.lastindex].split(","))
    n = len(buttons)
    m = len(joltage)

    prob = pulp.LpProblem(f"aoc25_day10_{p_id}", pulp.LpMinimize)
    x = [None]*n
    for i in range(n):
        x[i] = pulp.LpVariable(f"x{i}", 0, min(joltage[j] for j in buttons[i]), pulp.LpInteger)
    prob += sum(x)
    for j in range(m):
        prob += sum(x[i] for i in range(n) if j in buttons[i]) == joltage[j], f"b{j}"

    prob.solve()
    assert pulp.LpStatus[prob.status] == "Optimal"
    l = int(sum(v.varValue for v in prob.variables()))
    res += l

print(res)

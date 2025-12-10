import pulp

# Testcase: (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

b = [(3,), (1,3), (2,), (2,3), (0,2), (0,1)]
t = [3, 5, 4, 7]
n = len(b)
m = len(t)

prob = pulp.LpProblem("aoc25_day10_example", pulp.LpMinimize)
x = [None]*n
for i in range(n):
    x[i] = pulp.LpVariable(f"x{i}", 0, min(t[j] for j in b[i]), pulp.LpInteger)

prob += sum(x)
for j in range(m):
    prob += sum(x[i] for i in range(n) if j in b[i]) == t[j], f"b{j}"

prob.solve()

print("PuLP result:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print(int(sum(v.varValue for v in prob.variables())))

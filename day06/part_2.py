with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

ops = lines[-1].split()
funs = {"*": lambda x, y: x*y, "+": lambda x, y: x+y}
cols = len(ops)
w, h = len(lines[-1]), len(lines)-1
assert all(len(line) == w for line in lines)

res = 0
a = 0
for i in range(cols):
    b = w if i == cols-1 else (lines[-1].find(ops[i+1], a+1)-1)
    val = 1 if ops[i] == "*" else 0
    for j in range(a, b):
        y = int("".join(lines[k][j] for k in range(h)))
        val = funs[ops[i]](val, y)
    res += val
    a = b+1

print(res)

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ops = lines[-1].split()
funs = {"*": lambda x, y: x*y, "+": lambda x, y: x+y}
vals = [int(x) for x in lines[0].split()]
for line in lines[1:-1]:
    nums = [int(y) for y in line.split()]
    for i, y in enumerate(nums):
        vals[i] = funs[ops[i]](vals[i], y)

res = sum(vals)
print(res)

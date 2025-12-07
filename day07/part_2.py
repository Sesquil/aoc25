with open("input.txt", "r") as f:
    lines = f.readlines()

pos = {lines[0].index("S"): 1}
for line in lines[1:]:
    for x in [i for i, c in enumerate(line) if c == "^"]:
        if x in pos:
            v = pos.pop(x)
            for x_next in (x-1, x+1):
                if x_next in pos:
                    pos[x_next] += v
                else:
                    pos[x_next] = v
            res += v

res = sum(pos.values())
print(res)

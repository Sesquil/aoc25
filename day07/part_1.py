with open("input.txt", "r") as f:
    lines = f.readlines()

res = 0
pos = {lines[0].index("S")}
for line in lines[1:]:
    for x in [i for i, c in enumerate(line) if c == "^"]:
        if x in pos:
            pos.remove(x)
            pos.add(x-1)
            pos.add(x+1)
            res += 1

print(res)

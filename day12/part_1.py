import re

with open("example.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

regexp = re.compile(r"(\d+)x(\d+): (.+)")

def side_to_code(s):
    c = 0
    for i in range(len(s)):
        c *= 2
        c += 1 if s[i] == "#" else 0
    return c

def shape_codes(s):
    sides = [s[0]+s[1]+s[2], s[2]+s[5]+s[8], s[8]+s[7]+s[6], s[6]+s[3]+s[0]]
    print(sides)
    return [side_to_code(s) for s in sides]

shapes = []
line_id = 0
while line_id < len(lines):
    if "x" in lines[line_id]:
        break
    idx = int(lines[line_id][:-1])
    assert idx == len(shapes)
    line_id += 1
    shape = ""
    while lines[line_id] != "":
        shape += lines[line_id]
        assert(len(shape) % 3 == 0)
        line_id += 1
    shapes.append(shape_codes(shape))
    line_id += 1

num = len(shapes)
print(shapes)

res = 0
print(res)

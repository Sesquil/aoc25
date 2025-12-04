with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

res = 0
for line in lines:
    i, val = max(enumerate(line[:-1]), key=lambda it: it[1])
    val += max(line[i+1:])
    res += int(val)

print(res)

with open("input.txt", "r") as f:
    lines = f.readlines()

pos = 50
num = 0
"""
for line in lines:
    d, p = line[0], int(line[1:])
    s = -1 if d == "L" else 1
    for _ in range(p):
        pos = (pos + s) % 100
        if pos == 0:
            num += 1
"""
for line in lines:
    d, p = line[0], int(line[1:])
    num += p // 100
    p %= 100
    if d == "L": p = -p
    if pos != 0 and ((p < 0 and pos + p <= 0) or (p > 0 and pos + p >= 100)):
        num += 1
    pos = (pos + p) % 100
    
print(num)

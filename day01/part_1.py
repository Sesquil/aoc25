with open("input.txt", "r") as f:
    lines = f.readlines()

pos = 50
num = 0
for line in lines:
    d, p = line[0], int(line[1:])
    if d == "L": p = -p
    pos = (pos + p) % 100
    if pos == 0:
        num += 1

print(num)

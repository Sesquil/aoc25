with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ranges = []
ids = []
read_ids = False
for line in lines:
    if not line:
        read_ids = True
        continue
    if read_ids:
        ids.append(int(line))
    else:
        a, b = map(int, line.split("-"))
        ranges.append((a, b))
ranges.sort()

res = 0
for i in ids:
    for a, b in ranges:
        if a <= i and i <= b:
            res += 1
            break
        elif a > i:
            break

print(res)

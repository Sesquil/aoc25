with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ranges = []
ids = []
for line in lines:
    if not line:
        break
    a, b = map(int, line.split("-"))
    ranges.append((a, -1))
    ranges.append((b, 1))
ranges.sort()

res = 0
c = 0
a = 0
for r in ranges:
    c -= r[1]
    if r[1] < 0 and c == 1:
        a = r[0]
    elif r[1] > 0 and c == 0:
        res += r[0] - a + 1

print(res)

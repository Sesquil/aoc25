import re
import itertools

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"\[([.#]*)\](( \(\d+(,\d+)*\))+) \{(\d+(,\d+)*)\}")

res = 0
for line in lines:
    match = regexp.match(line)
    lights = match[1]
    buttons = [tuple(int(x) for x in s[1:-1].split(",")) for s in match[2].split()]
    #joltage = tuple(int(x) for x in match[match.lastindex].split(","))
    vals = [sum(1<<i for i in b) for b in buttons]
    val_dst = sum(1<<i for i, c in enumerate(lights) if c == "#")
    assert val_dst > 0

    n = len(lights)
    for l in range(1, n+1):
        found = False
        for val_set in itertools.combinations(vals, l):
            val_sum = 0
            for val in val_set:
                val_sum ^= val
            if val_sum == val_dst:
                found = True
                break
        if found:
            res += l
            break

print(res)

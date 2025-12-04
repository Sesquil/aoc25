with open("input.txt", "r") as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]

w, h = len(lines[0]), len(lines)

def check_field(x, y):
    if lines[y][x] != "@":
        return False
    n = 0
    for i in range(max(0, y-1), min(y+2, h)):
        for j in range(max(0, x-1), min(x+2, w)):
            if lines[i][j] == "@":
                n += 1
    return n <= 4

res, prev_res = 0, -1
while res != prev_res:
    prev_res = res
    for y in range(h):
        for x in range(w):
            if check_field(x, y):
                res += 1
                lines[y][x] = "."

print(res)

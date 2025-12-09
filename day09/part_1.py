with open("input.txt", "r") as f:
    lines = f.readlines()

pos = [tuple(map(int, line.split(","))) for line in lines]
n = len(pos)

def get_area(i, j):
    return (abs(pos[i][0] - pos[j][0]) + 1) * (abs(pos[i][1] - pos[j][1]) + 1)

res = 0
for i, j in ((i, j) for i in range(n) for j in range(i+1, n)):
    res = max(res, get_area(i, j))
print(res)

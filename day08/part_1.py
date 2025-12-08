with open("input.txt", "r") as f:
    lines = f.readlines()

def get_dist(x, y):
    return sum((x[i]-y[i])**2 for i in range(3))

def find_set(i):
    while sets[i][0] != i:
        i = sets[i][0]
    return i

p3d = [tuple(map(int, line.split(","))) for line in lines]
n = len(p3d)
m = 1000

pairs = [(get_dist(p3d[i], p3d[j]), i, j) for i in range(n) for j in range(i+1, n)]
pairs.sort()

sets = [[i, 1, False] for i in range(n)]
for _, i, j in pairs[:m]:
    a = find_set(i)
    b = find_set(j)
    if a != b:
        if sets[a][1] > sets[b][1]:
            a, b = b, a
        sets[a][0] = b
        sets[b][1] += sets[a][1]

sizes = [s[1] for s in sets]
sizes.sort()
res = sizes[-1]*sizes[-2]*sizes[-3]
print(res)

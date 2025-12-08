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

pairs = [(get_dist(p3d[i], p3d[j]), i, j) for i in range(n) for j in range(i+1, n)]
pairs.sort()

sets = [[i, 1, False] for i in range(n)]
for _, i, j in pairs:
    a = find_set(i)
    b = find_set(j)
    if a != b:
        if sets[a][1] > sets[b][1]:
            a, b = b, a
        sets[a][0] = b
        sets[b][1] += sets[a][1]
        if sets[b][1] == n:
            res = p3d[i][0]*p3d[j][0]
            break

print(res)

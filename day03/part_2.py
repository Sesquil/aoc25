with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

LEN = 12
res = 0
for line in lines:
    n = len(line)
    T = [[""]*(n+1) for _ in range(n)]
    for i in range(n-1, -1, -1):
        T[i][n-i] = line[i:]
        for j in range(1, min(n-i, LEN+1)):
            s = line[i] + T[i+1][j-1]
            if int(s) > int(T[i+1][j]):
                T[i][j] = s
            else:
                T[i][j] = T[i+1][j]
    val = max(T[i][LEN] for i in range(n-LEN+1))
    res += int(val)

print(res)

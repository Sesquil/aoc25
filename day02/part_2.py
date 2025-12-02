def sum_invalid_ids(a, b):
    res = 0
    for i in range(a, b+1):
        s = str(i)
        n = len(s)
        for m in range(1, n//2+1):
            if n % m == 0 and s[:m]*(n//m) == s:
                res += i
                break
    return res

with open("input.txt", "r") as f:
    line = f.read().strip()

ranges = [[int(i) for i in r.split("-")] for r in line.split(",")]

res = 0
for a, b in ranges:
    res += sum_invalid_ids(a, b)

print(res)

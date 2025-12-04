with open("input.txt", "r") as f:
    line = f.read().strip()

def sum_invalid_ids(a, b):
    res = 0
    for i in range(a, b+1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            res += i
    """
    i = a
    while i <= b:
        s = str(i)
        if len(s) % 2 == 1:
            n = (len(s) + 1) // 2 - 1
            i = int(2 * ("1" + n*"0"))
        else:
            if s[:len(s)//2] == s[len(s)//2:]:
                res += i
            i += 1
    """
    return res

ranges = [[int(i) for i in r.split("-")] for r in line.split(",")]

res = 0
for a, b in ranges:
    res += sum_invalid_ids(a, b)

print(res)

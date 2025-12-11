from collections import deque

with open("input.txt", "r") as f:
    lines = f.readlines()

def read_graph(lines):
    nodes = set()
    adj_out = {}
    for line in lines:
        i = line.find(":")
        v = line[:i]
        adj_out[v] = line[i+1:].split()
        nodes.add(v)
        nodes |= set(adj_out[v])
    for v in nodes:
        if not v in adj_out:
            adj_out[v] = []
    return adj_out

def topsort(adj_out):
    d_in = {v: 0 for v in adj_out}
    adj_in = {v: [] for v in adj_out}
    for v in adj_out:
        for w in adj_out[v]:
            d_in[w] += 1
            adj_in[w].append(v)
    queue = deque(v for v in adj_out if d_in[v] == 0)
    nodes = []
    while queue:
        v = queue.popleft()
        nodes.append(v)
        for w in adj_out[v]:
            d_in[w] -= 1
            if d_in[w] == 0:
                queue.append(w)
    return nodes, adj_in

def count_paths(nodes, adj_in, s, t):
    num_paths = {v: 0 for v in nodes}
    num_paths[s] = 1
    for v in nodes:
        for w in adj_in[v]:
            num_paths[v] += num_paths[w]
    return num_paths[t]

adj_out = read_graph(lines)
nodes, adj_in = topsort(adj_out)
assert len(nodes) == len(adj_out)

s, a, b, t = "svr", "fft", "dac", "out"
res_s_a = count_paths(nodes, adj_in, s, a)
res_s_b = count_paths(nodes, adj_in, s, b)
res_a_b = count_paths(nodes, adj_in, a, b)
res_b_a = count_paths(nodes, adj_in, b, a)
res_a_t = count_paths(nodes, adj_in, a, t)
res_b_t = count_paths(nodes, adj_in, b, t)

res = res_s_a * res_a_b * res_b_t + res_s_b * res_b_a * res_a_t
print(res)

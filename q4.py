def select_sum(r, T):
    v = 1
    s = 0
    c = 0
    while c <= r:
        if v >= T:
            s = s + v
        v = v * (r - c) // (c + 1)
        c = c + 1
    return s

data = list(map(int, input().split()))
n = data[0]
T = data[1]

total_all = 0
max_one = 0
max_row = n

for r in range(0, n+1):
    now = select_sum(r, T)
    total_all = total_all + now
    if now >= max_one:
        max_one = now
        max_row = r

print(total_all, max_one, max_row)
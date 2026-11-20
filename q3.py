def rising(n):
    p = 10
    while n > 0:
        d = n % 10
        if d >= p:
            return False
        p = d
        n = n // 10
    return True

def digit_sum(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s




data = list(map(int, input().split()))
L = data[0]
R = data[1]
k = data[2]

t = 0
total = 0
max_num = -1

for num in range(L, R + 1):
    if rising(num) == True:
        su = digit_sum(num)
        if su % k == 0:
            t = t + 1
            total = total + num
            if num > max_num:
                max_num = num

print(t, total, max_num)
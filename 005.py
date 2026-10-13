#求1000以内的偶数之和
total = 0
for i in range(2,1001):
    if i % 2 == 0:
        total += i
print(total)


def steps(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + steps(n // 2)
    return 1 +steps(n - 1)
print(steps(1024))



    
def fac(num):
    result = 1
    for i in range(2,num + 1):
        result *= i
    return result
m = int(input('m = '))
n = int(input('n = '))
x = fac(m) // fac(n) // fac(m - n)
print(x)

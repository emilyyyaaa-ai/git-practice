import math


def cf(x):
    
    return x * x - 5 * x + 4

x = float(input("请输入x的值："))



y1 = cf(2)
y2 = cf( x+ 5)
y3 = cf(math.sin(x))



print(f'y1 = {y1}')
print(f'y2 = {y2}')
print(f'y3 = {y3}')


#求两个整数的最大公约数
x = int(input("x="))
y = int(input("y="))
for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
        print(f"最大公因数为：{i}")
        break
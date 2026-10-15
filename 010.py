#斐波那契数
a,b = 0,1
for _  in range(20):
    a,b = b,a + b
    print(a)

#换种方法
a,b =0,1
while a <= 1000:
    a,b = b,a + b
    print(a)


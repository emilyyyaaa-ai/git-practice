def adjust(x,b):
    res = x +b
    return res
data = map(int,input().split())
n = data[0]
b = data[1]

cout_shi = 0






for i in range(1,n +1):
    x = int(input())
    t = adjust(x,b)

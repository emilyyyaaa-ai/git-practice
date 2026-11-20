def fee(x,t,p,q):
    if x <= t:
        return x * p
    else:
        return t * p + (x - t) * q

date = list(map(int,input().split()))
n,t1,t2,q1.q2 = 

total = 0
c2 = 0




for i in range(1,n + 1):
    x = int(input())
    f1 = fee(x,t1,p1,q1)
    f2 = fee(x,t2,p2,q2)
    if f1 > f2:
        choose = 1
        total += f1
    else:
        choose = 2
        total += f2
    print(f"选择{choose}")
    if choose = f2:
       c2 += 1
print(total,c2)




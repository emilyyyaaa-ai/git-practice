a,b,c = input("请输入三角形的三个边长：").split()
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("equilateral")
    if a != b or b != c or a != c:
        print("scalene")
    else:
        print("isosceles")
else:
    print("not a triangle")


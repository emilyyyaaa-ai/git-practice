year = int(input("请输入年份："))
if 1 <= year <= 9999:
    if year / 4 == 0 and year / 100 != 0:
        print("leap")
    elif year / 400 == 0:
        print("leap")
    else:
        print("common")
else:
    print("请输入正确年份")

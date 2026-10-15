
sizeNo = int(input())
quantity = int(input())
memberFlag = int(input())

# 判断输入是否合法
if sizeNo < 1 or sizeNo > 3 or quantity < 1 or quantity > 3 or memberFlag not in (0, 1):
    print("输入错误")
else:
    # 根据杯型确定单价
    if sizeNo == 1:
        price = 10
    elif sizeNo == 2:
        price = 12
    elif sizeNo == 3:
        price = 15

    total = price * quantity
    # 计算应付金额，满30减5
    if total >= 30:
        payable = total - 5
    else:
        payable = total
    # 判断赠送资格
    gift = 1 if (total >= 30 and memberFlag == 1) else 0

    # 按照要求格式输出
    print(f"原价金额： {total}")
    print(f"应付金额： {payable}")
    print(f"赠送小料： {gift}")
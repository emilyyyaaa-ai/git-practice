  

import random

money = 1000
print("Craps奶龙赌博游戏")
print("你有1000元的初始资金，当你的资金归0时：游戏结束!")
print("你是奶龙，将与黄色臭袋鼠决斗")
print("加油！奶龙")




while money > 0:
    print(f"\n你的总资产为: {money}元")
    # 下注循环
    while True:
        bet = int(input("请输入下注金额："))
        if 0 < bet <= money:
            break
        print("请输入大于0小于总资产的金额数！")

    #投掷骰子
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    first_point = d1 + d2
    print(f"第一次摇骰子，点数: {d1} + {d2} = {first_point}")

    if first_point in (7,11):
        print("奶龙牛逼！打败了臭袋鼠")
        money += bet
    elif first_point in (2,3,12):
        print("废物奶龙，你滴胆子真是肥嘟嘟的")
        money -= bet
    else:
        print(f"本轮目标点数是: {first_point},继续摇骰子")
        while True:
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            current = d1 + d2
            print(f"本轮奶龙的点数是: {d1} + {d2} = {current}")
            if current == 7:
                print("废物奶龙，你滴胆子真是肥嘟嘟的")
                money -= bet
                break
            elif current == first_point:
                print("奶龙牛逼（响起奶龙你魔性的笑声）")
                money += bet
                break

print("\n在不甘中，奶龙被臭袋鼠一脚踹死（响起奶龙的哀嚎）")  
#BMI计算器
height = float(input("请输入你的身高(cm):"))
weight = float(input("请输入你的体重(kg):"))
bmi = weight / (height/100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print("你的体重过轻")
elif bmi < 24:
    print("你的身材很棒")
elif bmi < 27:
    print("你的体重偏胖")    
elif bmi < 30:
    print("你中度肥胖")
else:
    print("你是良子吗")
        
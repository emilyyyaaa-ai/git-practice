num = 100

while num <= 999:
    low = num % 10
    mid = num // 10 % 10
    high = num // 100

    if num == low **3 +  mid **3 + high **3:
        print(num)
    num = num + 1



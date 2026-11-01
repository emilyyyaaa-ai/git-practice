import random


n = int(input("请输入下注次数："))
red_balls = [i for i in range(1,37)]
blue_balls = [i for i in range(1,17)]
for _ in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033\0m',end = '') 
    selected_balls = random.choice(blue_balls)
    print(f'\033[034m{ball:0>2d}\033\[0m') 
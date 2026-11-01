import random
counters = [0] * 6
for _ in range(6000):
    face =random.randrange(1,7)
    counters[face - 1] += 1
for _ in range(1,7):
    print(f"{face}点出现了{counters[face - 1]}次")    
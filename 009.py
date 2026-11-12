limit = 8
def select():
    limit = 3
    def allowed(number):
        return number < limit
    total = 0
    for number in range(1,6):
      if allowed(number):
        total += number
    return total

print(select(),limit)

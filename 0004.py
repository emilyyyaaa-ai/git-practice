def outer():
    total = 0
    def add():
        nonlocal total
        total += 2
        return total
    print(add(), add())
outer()

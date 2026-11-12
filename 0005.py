def outer():
    total = 0
    def inner():
        nonlocal total
        total += 1
        
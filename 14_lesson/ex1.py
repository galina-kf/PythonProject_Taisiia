def calculate_cart(**kwargs)->float:
    return sum(kwargs.values())

sum_cart = calculate_cart(bread=20.0, milk=50.0, appel=15.0)
print(sum_cart)
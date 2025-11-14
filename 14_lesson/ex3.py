x = 3
print(x)


def function():
    global x
    x = 5
    return x

print(function())

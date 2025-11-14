def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


def factorial_with_while(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(5))
print(factorial_with_while(5))
import random
from decorator_example import timing

numbers = [random.randint(1,100) for num in range(100_000)]

@timing
def sum_via_building_funktion():
    return sum(numbers)

@timing
def sum_via_for():
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_via_building_funktion())

print(sum_via_for())

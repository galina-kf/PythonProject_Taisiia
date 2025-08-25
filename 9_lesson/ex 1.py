import random

def throw_the_cube():
    return random.randint(1,6)

number = throw_the_cube()

while number < 5:
    print(f"you have number {number}")
    break

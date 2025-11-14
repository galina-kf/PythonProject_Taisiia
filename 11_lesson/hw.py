number = input('enter your number:')


def is_even(number):
    if int(number)%2 == 0:
        return True
    else:
        return False


print(is_even(number))
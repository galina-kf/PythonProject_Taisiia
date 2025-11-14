def greet(name,age):
    print(f'hello, {name.capitalize()}')
    print(f'your age is {age}')


def print_bye():
    print('Goodbye')


names = ['alex', 'bob', 'john']
for n in names:
    greet(n,25)
    print_bye()

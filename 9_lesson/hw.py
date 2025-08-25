start = input("Введіть початкове число: ")
stop = input("Введіть кінцеве число число: ")
numbers = range(int(start), int(stop))
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
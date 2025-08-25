mark = int(input("Please enter your mark(0-100): "))

if 90 <= mark <= 100:
    print("Відмінно")
elif 75 <= mark <= 89:
    print("Добре")
elif 60 <= mark <= 74:
    print("Задовільно")
elif mark <= 59:
    print("Спробуйте ще раз, перездача")

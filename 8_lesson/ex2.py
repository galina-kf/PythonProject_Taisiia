drinks = [
"Чай",
"Кава",
"Сік",
"Вода",
"Лимонад",
"Компот",
"Морс",
"Какао",
"Молоко",
"Квас",
"Узвар",
"Смузі"
]

for drink in drinks:
    if drink.endswith("о"):
        print(drink)
        break
possible_animals = ["кіт","собака","корова","качка","півень"]
animal = input("введить назву тварини:")
match animal:
    case "кіт":
        print("Мяу!")
    case "собака":
        print("Гав-гав!")
    case "корова":
        print( "Мууу!")
    case "качка":
        print("Кря-кря!")
    case "півень":
        print( "Ку-ку-рі-ку!")
    case _:
        print("Не знаю, як звучить ця тварина :(")

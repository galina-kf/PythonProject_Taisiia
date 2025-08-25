possible_colors = ["червоний", "зелений", "померанчевий"]
color = input("Введіть колір на світлофорі")
match color:
    case "червоний":
        print("стій")
    case "зелений":
        print ("можеш іти")
    case "померанчевий":
        print ("зачекай")
    case _:
        print("загрузка")
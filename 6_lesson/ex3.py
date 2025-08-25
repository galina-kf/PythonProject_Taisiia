temperature = int(input("Enter temperature in Celsius: "))
is_raining = input("Is it raining?(yes/no): ")
rain = is_raining.lower() == "yes"
no_rain = is_raining.lower() == "no"

if temperature < 5 or rain:
    print("надягни куртку та тепле взуття")
elif temperature < 20 and no_rain:
    print("надягни кофту та взуття")
elif (temperature > 20 and no_rain):
    print("надягнути футболку та сандалі")
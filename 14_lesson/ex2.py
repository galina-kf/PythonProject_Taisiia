#1. Local
#2. Enclosing
#3. Global
#4. build-in


first_name = "Ivan"
age = 500

def change():
    first_name = ("Mira")
    print(f"local variable is {first_name}")

print(f"global variable is {first_name}")
change()
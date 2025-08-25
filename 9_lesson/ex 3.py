
passwort = "coconat"
attempts = 3

for attempts in range(attempts):
    guess_passwort = input("Guess a pusswort:")


    if guess_passwort == passwort:
        print("richtig")
        break
    else:
        print("wrong password")
else:
    print("you lose")



#варианты решения
count = 3
while count > 0:
    #passwort
    count -= 1


for _ in range(count):
    #passwort
...
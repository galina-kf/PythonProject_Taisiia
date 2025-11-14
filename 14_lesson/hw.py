import random
from itertools import count

secret_number = random.randint(1,10)
count_attempts = 0

def create_game(secret_number: int):
    def guess():
        global count_attempts
        while True:
            try:
                player_number = int(input("введить число: "))
            except ValueError:
                print("Будь ласка, введіть ціле число.")
                continue

            count_attempts += 1

            if player_number == secret_number:
                print (f"Спроба {count_attempts}:Вгадав!")
                break
            elif player_number > secret_number:
                print(f"Спроба {count_attempts}:Загадане число менше")

            elif player_number < secret_number:
                print(f"Спроба {count_attempts}:Загадане число більше")

    return guess

game = create_game(secret_number)
game()

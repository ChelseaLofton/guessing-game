import random

secret_number = random.randint(1, 101)
print("Hello! What is your name?")
name = input("> ")
print(f"Hello {name}!")

while True:
    print("please choose a number between 1 and 100")
    guess = int(input("> "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Congrats {name}! You guessed the number!")
        break
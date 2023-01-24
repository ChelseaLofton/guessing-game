import random

# guesses_record = 0
lowest_score = []

def guess_number():
    secret_number = random.randint(1, 101)
    print("Hello! What is your name?")
    name = input("> ")
    print(f"Hello {name}!")
    num_guesses = 0

    while True:
        print("please choose a number between 1 and 100")
        guess = input("> ")
        if guess.isnumeric():
            guess = int(guess)
            if guess in range(1, 101):
                if guess > secret_number:
                    print("Too high!")
                    num_guesses += 1
                    print(num_guesses)
                elif guess < secret_number:
                    print("Too low!")
                    num_guesses += 1
                    print(num_guesses)
                else:
                    num_guesses += 1
                    print(f"Congrats {name}! You guessed the number! You got it in {num_guesses} guesses.")
                    lowest_score.insert(0, num_guesses) 
                    get_high_score(num_guesses)
                    break
            else:
                print("ERROR: Please only type a number between 1 and 100")
        else:
            print("ERROR: Please only type a number between 1 and 100")

def get_high_score(guesses):
    if lowest_score > guesses:
        lowest_score = guesses
        print(f"Your best score so far is : {lowest_score}")
        return lowest_score

def start_new():
    print("Would you like to play again? Type 'Yes' or 'No'")
    while True:
        answer = input("> ")
        if answer == "Yes":
            guess_number()
        elif answer == "No":
            break
        else:
            print("Error. Please type 'Yes' or 'No'")

guess_number() 
start_new()   
get_high_score()
import random
import art

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking a number between 1 and 100.")


def compare():
    number_of_lives = 0
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        number_of_lives = 10
        print("You have 10 attempts remaining to guess the number.")
    elif difficulty_level == "hard":
        print("You have 5 attempts remaining to guess the number.")
        number_of_lives = 5

    number = random.randint(1, 100)
    while number_of_lives > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Too high. \nGuess again.")
            print(f"You have {number_of_lives} attempts to guess the number")
        elif user_guess < number:
            print("Too low. \nGuess again.")
            print(f"You have {number_of_lives} attempts to guess the number.")
        elif user_guess == number:
            print(f"You got it! The answer was {number}")
            number_of_lives = 0
        number_of_lives -= 1



compare()







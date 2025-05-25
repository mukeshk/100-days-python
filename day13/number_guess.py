from random import randint
import art
print(art.task_art)


print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100")
game_difficulty= input("Choose a difficulty. type 'easy' or 'hard':")
guess_attempts_left = 0
if game_difficulty == 'easy':
    guess_attempts_left = 10
else:
    guess_attempts_left = 5

number_guessed = False
number_to_guess = randint(1,100)
print(f"You have {guess_attempts_left} attempts left")
while number_guessed == False and guess_attempts_left> 0:
    guessed_number = int(input("Make a guess"))
    guess_attempts_left-=1
    if number_to_guess == guessed_number:
        number_guessed = True
        print("Number guessed...")
    elif number_to_guess > guessed_number:
        print("Too low")
    elif number_to_guess < guessed_number:
        print("Too high")

if number_guessed :
    print(f"You have guess the number correctly")
else:
    print(f"You have guess the number incorrectly")

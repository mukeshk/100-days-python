import random

word_list = ["sample","wrangle","monsoon"]
is_game_on = True
no_of_lives = 6

HANGMAN_PICS = [
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
========
""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
========
""",
    """
    +---+
    |   |
    O   |
       |
        |
========
""",
    """
    +---+
    |   |
    O   |
       |
       |
========
""",
    """
    +---+
    |   |
       |
       |
       |
========
"""
]


def print_hangman(stage):
  """Prints the hangman ASCII art for a given stage."""
  if stage < 0 or stage >= len(HANGMAN_PICS):
    print("Invalid hangman stage.")
    return

  print(HANGMAN_PICS[stage])




word_to_guess = random.choice(word_list)
#guessed_word = "_" * len(word_to_guess)
guessed_word = ['X'] * len(word_to_guess)

def find_all_chars(word, char):
    return [index for index, c in enumerate(word) if c == char]

def render_word_to_guess():
    print(f"Guess the word:= {guessed_word}. length of word = {len(guessed_word)}")

def all_word_guessed():
    if 'X' in guessed_word:
        return False
    else :
        return True

while is_game_on:
    render_word_to_guess()

    guessed_char = input("Guess any letter:").lower()
    matched_indexes =  find_all_chars(word_to_guess,guessed_char)
    if len(matched_indexes) == 0:
        print("wrong guess")
        no_of_lives -= 1
        if no_of_lives == 0:
            print("You lose. Better luck next time")
            is_game_on = False
    else:
        print("right guess")
        for idx in matched_indexes:
            guessed_word[idx]=guessed_char
        if all_word_guessed():
            print(f"You win.You rock!! Word = {word_to_guess}")
            is_game_on = False

    print_hangman(no_of_lives)




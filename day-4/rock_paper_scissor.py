import random
# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""";

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_symbols = [rock,paper,scissor]

def print_chosen_symbol(choice):
    if 2 >= choice >= 0:
        print(game_symbols[choice])
    else:
        print("Your choice is incorrect")

user_choice = int(input("What do you choose Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0,2)

print("You choose:")
print_chosen_symbol(user_choice)

print(f"Computer chooses: {computer_choice}")
print_chosen_symbol(computer_choice)

if user_choice == 0 and computer_choice == 2 :
   print("You win !!")
elif user_choice == 2 and computer_choice == 1:
   print("You win !!")
elif user_choice == 1 and computer_choice == 0:
    print("You win !!")
elif user_choice == computer_choice:
    print("Its a draw!")
elif user_choice > 2 :
    print(" Your input was incorrect!")
else :
    print("Computer wins!!")

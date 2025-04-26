print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

step_1_choice = input('You\'re at a cross road. Where do you want to go type "left" or "right"? ')
if step_1_choice == 'left' or step_1_choice == 'LEFT':
    step_2_choice = input('''
    You have come to a lake. There is a island in the middle of lake.\r\n 
    Type "swim" to swim across.\r\n
    Type "wait" for a boat to wait for a boat to swim or wait?''')
    if step_2_choice == 'wait' or step_2_choice == 'WAIT':
        step_3_choice = input("Which door? Red, Blue, or Yellow:")
        if step_3_choice == 'Red' or step_3_choice == 'RED':
            print("Burned by fire.Game over.")
        elif step_3_choice == 'Blue' or step_3_choice == 'BLUE':
            print("Eaten by beasts. Game over.")
        elif step_3_choice == 'Yellow' or step_3_choice == 'YELLOW':
            print("You win.")
        else:
            print("Game over")
    else:
        print("You are attacked by trout. Game over")
else :
    print("You fall into a hole. Game over.")
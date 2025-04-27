#https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Hurdle%201&url=%2Fworlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_a_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for _ in range(0 ,6):
    jump_a_hurdle()

# def func turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

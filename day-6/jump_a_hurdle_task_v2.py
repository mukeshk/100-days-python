def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_a_hurdle():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_a_hurdle()
    else:
        move()
# def func turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

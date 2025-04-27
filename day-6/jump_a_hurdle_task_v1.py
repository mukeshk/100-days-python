def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_a_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_a_hurdle()
    else:
        move()

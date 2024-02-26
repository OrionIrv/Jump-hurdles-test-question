from library import turn_right, jump_hurdles

while not at_goal():  #while not at the goal
    if front_is_clear():  #and the front is clear
        move()  #move
    else:    #if not
        jump_hurdles()
else:   #if at the goal
    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_hurdles():
    turn_left()
    while wall_on_right():
        move()
    else:
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
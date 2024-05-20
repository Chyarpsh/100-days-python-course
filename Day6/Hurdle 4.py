def turn_right():
    turn_left() # type: ignore
    turn_left() # type: ignore
    turn_left() # type: ignore
    
def jump():
    turn_left() # type: ignore
    while wall_on_right(): # type: ignore
          move() # type: ignore
    turn_right()
    move() # type: ignore
    turn_right()
    
    while front_is_clear(): # type: ignore
          move() # type: ignore
    
    turn_left() # type: ignore

while not at_goal(): # type: ignore
    if  wall_in_front(): # type: ignore
        jump()
    else:
        move() # type: ignore
    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

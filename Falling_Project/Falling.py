# Simple Falling Skies Project with Turtle

import turtle

window = turtle.Screen() # creating Screen
window.title('Falling Skies') # creating title
window.bgcolor('blue') # creating backgroundcolor
window.setup(width=800, height=600)
window.tracer(0) # screen does not update until you activate the update method


player = turtle.Turtle() # adding the player
player.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
player.shape('square')
player.color('white')
player.penup() # turtle stops drawing lines. Has to be before the goto command
player.goto(0, -250) # in turtle 0, 0 is the center so in this case the player starts at the bottom center
player.direction = 'stop' # player does not move withoput any commands at the start

good_guy = turtle.Turtle() # adding the player
good_guy.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
good_guy.shape('circle')
good_guy.color('black')
good_guy.penup() # turtle stops drawing lines. Has to be before the goto command
good_guy.goto(0, 250) # in turtle 0, 0 is the center so in this case the player starts at the bottom center


# Functions
def go_left():
    player.direction = 'left'

def go_right():
    player.direction = 'right'

#Keyboard Bindings
window.listen()
window.onkeypress(go_left, 'Left') # using arrow keys
window.onkeypress(go_right, 'Right') # using arrow keys

# Main game loop:
while True:
    # Update screen
    window.update()
    # Move the player
    if player.direction == 'left':
        x = player.xcor() # find the current x coordinate of the player
        x -= 3 # at the start the position of x = 0 and after subtracting its -3
        player.setx(x) # we set the player to -3

    if player.direction == 'right':
        x = player.xcor() # find the current x coordinate of the player
        x += 3 
        player.setx(x)
    
    # Move the good guy
 
    
    

window.mainloop()
# Simple Falling Skies Project with Turtle

import turtle
import random
import os

score = 0
lives = 3
paused = False
running = True

window = turtle.Screen() # creating Screen
window.title('Falling Skies') # creating title
window.bgcolor('blue') # creating backgroundcolor
window.bgpic('africa_background.gif') #implementing background picture for much more realistic immersion
window.setup(width=800, height=600)
window.tracer(0) # screen does not update until you activate the update method

window.register_shape('Lion-in-a-Box.gif')
window.register_shape('meat.gif')
window.register_shape('hunter.gif')

player = turtle.Turtle() # adding the player
player.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
player.shape('Lion-in-a-Box.gif')
player.color('white')
player.penup() # turtle stops drawing lines. Has to be before the goto command
player.goto(0, -250) # in turtle 0, 0 is the center so in this case the player starts at the bottom center
player.direction = 'stop' # player does not move withoput any commands at the start

# Create a list of good guys
good_guys = []

# Add the good guys to the list
for _ in range(20):
    good_guy = turtle.Turtle() # adding the player
    good_guy.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
    good_guy.shape('meat.gif') # adding meat picture 
    good_guy.color('black')
    good_guy.penup() # turtle stops drawing lines. Has to be before the goto command
    good_guy.goto(-100, 250) # in turtle 0, 0 is the center so in this case the player starts at the bottom center
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)


# Create a list of bad guys
bad_guys = []

# Add the good guys to the list
for _ in range(20):
    bad_guy = turtle.Turtle() # adding the player
    bad_guy.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
    bad_guy.shape('hunter.gif')
    bad_guy.color('red')
    bad_guy.penup() # turtle stops drawing lines. Has to be before the goto command
    bad_guy.goto(100, 250) # in turtle 0, 0 is the center so in this case the player starts at the bottom center
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)

# Make the scoreboard
pen = turtle.Turtle() # adding the player
pen.hideturtle()
pen.speed(0) # With this command its drawing as fast as its can. Hs to be the first command before its drawing
pen.shape('circle')
pen.color('black')
pen.penup() # turtle stops drawing lines. Has to be before the goto command
pen.goto(0, 260)
pen.write('Score: {} Lives: {}'.format(score, lives), align='center', font=('courier', 24, 'normal')) 


# Functions
def go_left():
    player.direction = 'left'

def go_right():
    player.direction = 'right'

def quit(): # sets the command when pressing q its changing from True to False
    global running
    running = False

def toggle_pause(): # sets the command when pressing p its changing from False to True
    global paused
    if paused == True:
        paused = False
    else:
        paused = True

#Keyboard Bindings
window.listen()
window.onkeypress(go_left, 'Left') # using arrow keys
window.onkeypress(go_right, 'Right') # using arrow keys

window.onkeypress(quit, 'q')

window.onkeypress(toggle_pause, 'p')

# Main game loop:
while running:
    if not paused:
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
        
        # Move the good guys
        for good_guy in good_guys:
            y = good_guy.ycor()
            y -= good_guy.speed
            good_guy.sety(y)

            # Check if off screen
            if y < -300:
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                good_guy.goto(x, y)


            # Check for collision with the player
            if good_guy.distance(player) < 40:
                os.system('afplay Score3.mp3&')
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                good_guy.goto(x, y)
                score += 1
                pen.clear()
                pen.write('Score: {} Lives: {}'.format(score, lives), align='center', font=('courier', 24, 'normal')) 

        # Move the bad guys
        for bad_guy in bad_guys:
            y = bad_guy.ycor()
            y -= bad_guy.speed
            bad_guy.sety(y)

            # Check if off screen
            if y < -300:
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                bad_guy.goto(x, y)


            # Check for collision with the player
            if bad_guy.distance(player) < 40:
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                bad_guy.goto(x, y)            
                lives -= 1
                pen.clear()
                pen.write('Score: {} Lives: {}'.format(score, lives), align='center', font=('courier', 24, 'normal'))
    else:
        window.update()

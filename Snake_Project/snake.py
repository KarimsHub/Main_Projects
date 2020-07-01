# Simple Snake Game with Turtle

# Importing modules
import turtle
import time
import random
import os

delay = 0.1
running = True # created the variable for main loop which can be changed
paused = False # created a variable to pause the game

# Score
score = 0
high_score = 0

# set up the screen
window = turtle.Screen()
window.title('Snake Game by Karim')
window.bgcolor('white')
window.setup(width = 600, height = 600)
window.tracer(0) #turns off the screen updates/ turtle animation

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square') #determine the form of the displayed body
head.color('blue')
head.penup() #does not draw anything
head.goto(0,0) #head starts in the center of the screen
head.direction = 'stop'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup() #does not draw anything
food.goto(0,100) #food starts at another position than head

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align = 'center', font = ('Arial', 24, 'normal'))

# functions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'



def move():
    if head.direction == 'up':
        y = head.ycor() # return the turtles y coordinate
        head.sety(y + 20) #In this case if turtle goes up it moves by 20 each time

    if head.direction == 'down':
        y = head.ycor() # return the turtles y coordinate
        head.sety(y - 20) 

    if head.direction == 'left':
        x = head.xcor() # return the turtles x coordinate
        head.setx(x - 20) 

    if head.direction == 'right':
        x = head.xcor() # return the turtles x coordinate
        head.setx(x + 20) 

def quit(): # sets the command when pressing q its changing from True to False
    global running
    running = False

def toggle_pause(): # sets the command when pressing p its changing from False to True
    global paused
    if paused == True:
        paused = False
    else:
        paused = True

# Keyboard bindings
window.listen() # set focus on turtlescreen in order to collect key events. Needed to to be able to register key-events
window.onkeypress(go_up, 'w') # bind the function go_up to key-press event w, a, s, d
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

window.onkeypress(quit, 'q')
window.onkeypress(toggle_pause, 'p')

# Main game loop
while running:
    if not paused:

        window.update() #Perform a turtlescreen update. used when tracer is turned off, like in our case


        # check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            os.system('afplay Failure_sound.mp3&')
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000) # moving the segments out of the screen
        
            # clear the segments list
            segments.clear()

            # Reset score if it colide with the border
            score = 0

            # Update the score board
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align = 'center', font = ('Arial', 24, 'normal'))

        if head.distance(food) < 20: #build in function to measure the distance between head and food to check for a collision
            #move the food to random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)

            food.goto(x, y)
            # implement music
            os.system('afplay Score3.mp3&')

            #add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('grey')
            new_segment.penup()
            segments.append(new_segment)

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align = 'center', font = ('Arial', 24, 'normal'))

        # move the end segements first
        for index in range(len(segments)-1, 0, -1): # for example if list contains 10 it decimate by 1 and goes up to 0 (but 0 is +1 so we have to decimate by 1 again)
            x = segments[index-1].xcor() # moving each segment where the last one was so -1 
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # move segment 0 where the head is
        if len(segments) > 0: #only working if there are more than one segment
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y) #moves segment 0 to the head corrdinates (x and y)
        
        move()

        # Check for head collision with the body
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = 'stop'
                # hide the segments
                for segment in segments:
                    segment.goto(1000, 1000) # moving the segments out of the screen
        
                # clear the segments list
                segments.clear()

                # Reset score if it colide with the body
                score = 0
                
                # Update the score board
                pen.clear()
                pen.write('Score: {}  High Score: {}'.format(score, high_score), align = 'center', font = ('Arial', 24, 'normal'))

        time.sleep(delay) #suspend execution of the program by the given number of seconds
    else:
        window.update()
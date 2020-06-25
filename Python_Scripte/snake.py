# Simple Snake Game with Turtle

import turtle
import time
import random

delay = 0.1

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



# functions

def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
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


# Keyboard bindings
window.listen() # set focus on turtlescreen in order to collect key events. Needed to to be able to register key-events
window.onkeypress(go_up, 'w') # bind the function go_up to key-press event w, a, s, d
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

# Main game loop
while True:
    window.update() #Perform a turtlescreen update. used when tracer is turned off, like in our case


    # check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # moving the segments out of the screen
    
        # clear the segments list
        segments.clear()

    if head.distance(food) < 20: #build in function to measure the distance between head and food to check for a collision
        #move the food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        food.goto(x, y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

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

    time.sleep(delay) #suspend execution of the program by the given number of seconds

window.mainloop()
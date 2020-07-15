

import turtle
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # setting up the size of the screen

window = turtle.Screen() # creating the window
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.title('Space Arena') # adding the title
window.bgcolor('black') # adding the backgroundcolor
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle() # we won't see the drawed lines 

class Sprite(): # the class for objects like player, enemy etc.
    # the constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0 # horizontal speed (if dx is positiv the object moves to the right, if negative left)
        self.dy = 0 # vertical speed (if dy is positiv the object moves up, if negative down)
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.02

    
    def update(self):
        self.heading += self.da # the heading is gonna change by the delta of the angle
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
    
        self.x += self.dx
        self.y += self.dy 

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading) # sets the orientation of the turle to east
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

class Player(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3 # only the player has lives and score
        self.score = 0
        self.heading = 90 #player goes up
        self.da = 0 # changing the angle
    
    def rotate_left(self):
        self.da = 5

    def rotate_right(self):
        self.da = -5

    def stop_rotation(self):
        self.da = 0
    
    def accelerate(self):
        self.thrust += self.acceleration
    
    def deaccelerate(self):
        self.thrust = 0.0
    
    def render(self, pen):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading) # sets the orientation of the turle to east
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

        pen.shapesize(1.0, 1.0, None)


# Creating the player sprite as a spaceship
player = Player(0,0, 'triangle', 'white') # putting the player in the center

enemy = Sprite(0,100, 'square', 'red')
enemy.dx = -1
enemy.dy = -0.3

powerup = Sprite(0,-100, 'circle', 'blue')
powerup.dy = 1
powerup.dx = 0.1

# Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)

# Keyboard bindings
window.listen()
window.onkeypress(player.rotate_left, 'Left')
window.onkeypress(player.rotate_right, 'Right')

window.onkeyrelease(player.stop_rotation, 'Left') # the moment you dont press left or right it will stop rotating!
window.onkeyrelease(player.stop_rotation, 'Right')

window.onkeypress(player.accelerate, 'Up')
window.onkeyrelease(player.deaccelerate, 'Up')
# Main Loop
while True:
    # Clear the screen
    pen.clear()

    # Update the Sprites to move around the screen
    for sprite in sprites:
        sprite.update()


    # Render the Sprites
    for sprite in sprites:
        sprite.render(pen)

    # Update the Screen
    window.update()


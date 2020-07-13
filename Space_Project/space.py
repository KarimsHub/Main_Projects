

import turtle


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
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

# Creating the player sprite as a spaceship
player = Sprite(0,0, 'triangle', 'white') # putting the player in the center
player.dx = 1
player.dy = 0.5

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




import turtle
import math
import random


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

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
    
    def start_level(self):
        sprites.clear() # clears all the sprites from the list

        # add the player 
        sprites.append(player)

        # add missile
        sprites.append(missile)

        # add enemy per level
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Enemy(x, y, 'square', 'red'))
            sprites[-1].dx = dx # will give us the the last sprite what was added
            sprites[-1].dy = dy

        # add powerup per level
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Powerup(x, y, 'circle', 'blue'))
            sprites[-1].dx = dx # will give us the the last sprite what was added
            sprites[-1].dy = dy




    def render_border(self):
        pen.color('white')
        pen.width(3)
        pen.penup()

        left = -self.width / 2 # if the screen width is 800 like in  our case its -400 left and 400 by the right side
        right = self.width / 2
        top = self.height / 2
        bottom = -self.height / 2

        pen.goto(left, top) # starting left top
        pen.pendown() # function needed so we can actually draw the border
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

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
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20


    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    
    def update(self):
        self.heading += self.da # the heading is gonna change by the delta of the angle
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
    
        self.x += self.dx
        self.y += self.dy

        self.border_check()
    
    def border_check(self):
        if self.x > game.width / 2 - 10:
            self.x = game.width /2 - 10
            self.dx *= -1 # the sprite bounces off the right wall
        
        elif self.x < -game.width / 2 + 10:
            self.x = -game.width /2 + 10
            self.dx *= -1 # the sprite bounces off the left wall       

        if self.y > game.height / 2 - 10:
            self.y = game.height /2 - 10
            self.dy *= -1 # the sprite bounces off the top wall
        
        elif self.y < -game.height / 2 + 10:
            self.y = -game.height /2 + 10
            self.dy *= -1 # the sprite bounces off the bottom wall       


    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading) # sets the orientation of the turle to east
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

        self.render_health_meter(pen)

    
    def render_health_meter(self, pen):
        # Draw health
        pen.goto(self.x -10, self.y + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)

        if self.health/self.max_health < 0.3:
            pen.color('red') # if the health reaches under 30% the pen color changes to red
        elif self.health/self.max_health < 0.7:
            pen.color('yellow')
        else:
            pen.color('green')
        
        pen.fd(20 * (self.health/self.max_health))

        if self.health != self.max_health: # if function neccessary to get rid of the grey dots at the start
            pen.color('grey')
            pen.fd(20 * ((self.max_health - self.health)/self.max_health))
        
        pen.penup()

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
    
    def fire(self):
        missile.fire(self.x, self.y, self.heading, self.dx, self.dy) # missile starting on the same position as the player sprites
    
    def render(self, pen):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading) # sets the orientation of the turle to east
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

        pen.shapesize(1.0, 1.0, None)

        self.render_health_meter(pen)

class Missile(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = 'ready'
        self.thrust = 8.0
        self.max_fuel = 200
        self.fuel = self.max_fuel
        self.height = 4
        self.width = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == 'ready':
            self.state = 'active'
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust # taking the current dx (which is from playwer) and adds own thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
       if self.state == 'active':
           self.fuel -= self.thrust
           if self.fuel <= 0:
               self.reset()
           self.heading += self.da # the heading is gonna change by the delta of the angle
           self.heading %= 360
           
           self.x += self.dx
           self.y += self.dy
           
           self.border_check()
    
    def reset(self): # once its resets we set the fuel back to max fuel and state to ready
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = 'ready'


    def render(self, pen): # only renders if its active
        if self.state == 'active':
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x, self.y)
            pen.setheading(self.heading) # sets the orientation of the turle to east
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp() # puts the pen on the screen
    
            pen.shapesize(1.0, 1.0, None)

class Enemy(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Powerup(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

# Create the border
game = Game(600, 400)

# Creating the player sprite as a spaceship
player = Player(0,0, 'triangle', 'white') # putting the player in the center

# Creating missile object
missile = Missile(0, 100, 'circle', 'yellow')

#enemy = Enemy(0,100, 'square', 'red')
#enemy.dx = -1
#enemy.dy = -0.3
#
#enemy2 = Enemy(-100,100, 'square', 'red')
#enemy2.dx = 1
#enemy2.dy = 0.3

#powerup = Powerup(0,100, 'circle', 'blue')
#powerup.dy = 1
#powerup.dx = 0.1
#
#powerup2 = Powerup(-100,100, 'circle', 'blue')
#powerup2.dy = -1
#powerup2.dx = -0.1

# Sprites list
sprites = []
#sprites.append(player)
#sprites.append(enemy)
#sprites.append(powerup)
#sprites.append(missile)
#sprites.append(enemy2)
#sprites.append(powerup2)

# setup the level
game.start_level()

# Keyboard bindings
window.listen()
window.onkeypress(player.rotate_left, 'Left')
window.onkeypress(player.rotate_right, 'Right')

window.onkeyrelease(player.stop_rotation, 'Left') # the moment you dont press left or right it will stop rotating!
window.onkeyrelease(player.stop_rotation, 'Right')

window.onkeypress(player.accelerate, 'Up')
window.onkeyrelease(player.deaccelerate, 'Up')

window.onkeypress(player.fire, 'space')

# Main Loop
while True:
    # Clear the screen
    pen.clear()

    # Update the Sprites to move around the screen
    for sprite in sprites:
        sprite.update()
    
    # check for collision
    for sprite in sprites:
        if isinstance(sprite, Enemy):
            if player.is_collision(sprite):
                player.x = 0
                player.y = 0

            if missile.state == 'active' and missile.is_collision(sprite):
                sprite.x = -100
                sprite.y = -100
                missile.reset()
        
        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                sprite.x = 100
                sprite.y = 100

            if missile.state == 'active' and missile.is_collision(sprite):
                sprite.x = 100
                sprite.y = -100
                missile.reset()


    # Render the Sprites
    for sprite in sprites:
        sprite.render(pen)

    # Render the borders
    game.render_border()

    # Update the Screen
    window.update()


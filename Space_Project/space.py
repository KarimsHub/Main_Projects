

import turtle
import math
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # setting up the size of the screen

window = turtle.Screen() # creating the window
window.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20)
window.title('Space Arena') # adding the title
window.bgcolor('black') # adding the backgroundcolor


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
        self.state = 'splash'
    
    def start_level(self):
        sprites.clear() # clears all the sprites from the list

        # add the player 
        sprites.append(player)

        # add missile
        for missile in missiles:
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




    def render_border(self, pen, x_offset, y_offset):
        pen.color('white')
        pen.width(3)
        pen.penup()

        left = -self.width / 2 - x_offset# if the screen width is 800 like in  our case its -400 left and 400 by the right side
        right = self.width / 2 - x_offset
        top = self.height / 2 - y_offset
        bottom = -self.height / 2 - y_offset

        pen.goto(left, top) # starting left top
        pen.pendown() # function needed so we can actually draw the border
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()
    
    def render_info(self, pen, score, active_enemies = 0):
        pen.color('#222255') # using html hex code
        pen.penup()
        pen.goto(400,0)
        pen.shape('square')
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()

        pen.color('white')
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color('white')
        character_pen.scale = 1.0
        character_pen.draw_string(pen, 'SPACE GAME', 400, 270)
        character_pen.draw_string(pen, 'SCORE {}'.format(score), 400, 240)
        character_pen.draw_string(pen, 'ENEMIES {}'.format(active_enemies), 400, 210)
        character_pen.draw_string(pen, 'Lives {}'.format(player.lives), 400, 180)
        character_pen.draw_string(pen, 'Level {}'.format(game.level), 400, 150)

    def start(self):
        self.state = 'playing'         

class CharacterPen(): # defining all of the shapes
    def __init__(self, color = 'white', scale = 1.0):
        self.color = color
        self.scale = scale

        self.characters = {} # creating a dictionary
        self.characters['1'] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10)) # drawing these lines because of performance issues by rendering
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))   
        
        self.characters["-"] = ((-3, 0), (3, 0)) 


    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color) # picks the color we set the object earlier

        # center the text
        x -= 15 * self.scale * ((len(str)-1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

    def draw_character(self, pen, character, x, y):
        scale = self.scale # might want some characters bigger than others

        if character in 'abcdefghijklmnopqrstuvwxyz':
            scale *= 0.8 # maing the lower case character 80% the size of the upper ones
            
        character = character.upper() # we want any character as an uppercase letter
        # check if the character is in the dictionary
        if character in self.characters:
            pen.penup()
            xy = self. characters[character][0] # gives us the coordinates we have declared f.e. xy for 1 is (-5,10)
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self. characters[character][i] 
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()                   

#Splash Screen
character_pen = CharacterPen('red', 3.0)
character_pen.draw_string(pen, 'SPACE GAME', 0, 160)

character_pen.scale = 1.0
character_pen.draw_string(pen, 'BY KARIM', 0, 100)

pen.color('white')
pen.shape('triangle')
pen.goto(-150, 20)
pen.stamp()

character_pen.draw_string(pen, 'Player', -150, -20)

pen.color('orange')
pen.shape('square')
pen.goto(0, 20)
pen.stamp()
character_pen.draw_string(pen, 'Enemy', 0, -20)

pen.color('blue')
pen.shape('circle')
pen.goto(150, 20)
pen.stamp()
character_pen.draw_string(pen, 'Powerup', 150, -20)

character_pen.draw_string(pen, 'Up Arrow', -100, -60)
character_pen.draw_string(pen, 'Accelerate', 100, -60)
character_pen.draw_string(pen, 'Left Arrow', -100, -100)
character_pen.draw_string(pen, 'Rotate Left', 100, -100)
character_pen.draw_string(pen, 'Right Arrow', -100, -140)
character_pen.draw_string(pen, 'Rotate Right', 100, -140)
character_pen.draw_string(pen, 'Space', -100, -180)
character_pen.draw_string(pen, 'Fire', 100, -180)
character_pen.draw_string(pen, 'PRESS S TO START', 0, -240)
character_pen.draw_string(pen, '', 0, 0)

window.tracer(0)


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
        self.state = 'active'
        self.radar = 200
        self.max_dx = 4
        self.max_dy = 4


    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False
    
    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dx = temp_dx
        other.dy = temp_dy

    
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


    def render(self, pen, x_offset, y_offset):
        if self.state == 'active':
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading) # sets the orientation of the turle to east
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp() # puts the pen on the screen

            self.render_health_meter(pen, x_offset, y_offset)

    
    def render_health_meter(self, pen, x_offset, y_offset):
        # Draw health
        pen.goto(self.x - x_offset -10, self.y - y_offset + 20)
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
        num_of_missiles = 0
        for missile in missiles:
            if missile.state == 'ready':
                num_of_missiles += 1
        
        for missile in missiles:
            # 1 missile ready
            if num_of_missiles == 1:
                missile.fire(self.x, self.y, self.heading, self.dx, self.dy) # missile starting on the same position as the player sprites
                break
            # 2 missiles ready
            if num_of_missiles == 2:
                directions = [-5, 5] # we just want them spreading left and right
                for missile in missiles:
                    if missile.state == 'ready':         
                        missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy) # missile starting on the same position as the player sprites
                    
            # 3 missiles ready
            if num_of_missiles == 3:
                directions = [0, -5, 5] # spreading in the left, right, middle
                for missile in missiles:
                    if missile.state == 'ready':
                        missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy) # missile starting on the same position as the player sprites
                    

    def update(self):
        if self.state == 'active':
            self.heading += self.da # the heading is gonna change by the delta of the angle
            self.heading %= 360
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            self.x += self.dx
            self.y += self.dy
            self.border_check()
            # Check health
            if self.health <= 0:
                self.reset()
    
    def reset(self): # resetting everything to the default numbers
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

    def render(self, pen, x_offset, y_offset):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.setheading(self.heading) # sets the orientation of the turle to east
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp() # puts the pen on the screen

        pen.shapesize(1.0, 1.0, None)

        self.render_health_meter(pen, x_offset, y_offset)

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


    def render(self, pen, x_offset, y_offset): # only renders if its active
        if self.state == 'active':
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading) # sets the orientation of the turle to east
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp() # puts the pen on the screen
    
            pen.shapesize(1.0, 1.0, None)

class Enemy(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = 20
        self.health = self.max_health
        self.type = random.choice(['hunter', 'mine', 'surveillance'])

        if self.type == 'hunter':
            self.color = 'red'
            self.shape = 'square'
        elif self.type == 'mine':
            self.color = 'orange'
            self.shape = 'square'
        elif self.type == 'surveillance':
            self.color = 'pink'
            self.shape = 'square'

    def update(self):
        if self.state == 'active':
            self.heading += self.da # the heading is gonna change by the delta of the angle
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # Check health
            if self.health <= 0:
                self.reset()
            
            # for different enemy types
            if self.type == 'hunter': # they should go after the player
                if self.x < player.x: # the hunter is to left of the player
                    self.dx += 0.05 # numbers depending of your system speed
                else:
                    self.dx -= 0.05
                
                if self.y < player.y:
                    self.dy += 0.05
                else:
                    self.dy -= 0.05 
            elif self.type == 'mine':
                self.dx = 0
                self.dy = 0
            
            elif self.type == 'surveillance': # they should avoid the player by deault
                if self.x < player.x:
                    self.dx -= 0.05 
                else:
                    self.dx += 0.05
                
                if self.y < player.y:
                    self.dy -= 0.05
                else:
                    self.dy += 0.05
            
            # Set max speed
            if self.dx > self.max_dx:
                self.dx = self.max_dx
            elif self.dx < -self.max_dx:
                self.dx = -self.max_dx
            
            if self.dy > self.max_dy:
                self.dy = self.max_dy
            elif self.dy < -self.max_dy:
                self.dy = -self.max_dy

    
    def reset(self):
        self.state = 'inactive'

class Powerup(Sprite): # inherets the attributes from the parent class
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update(self, x, y):
        self.x = x
        self.y = y

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def render(self, pen, sprites):

        # Draw radar circle
        pen.color('white')
        pen.setheading(90)
        pen.goto(self.x + self.width / 2, self.y)
        pen.pendown()
        pen.circle(self.width / 2)
        pen.penup()

        # Draw the sprites
        for sprite in sprites:
            if sprite.state == 'active': # just want to use the active sprites
                radar_x = self.x + (sprite.x - player.x) * (self.width / game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height / game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color) # getting the actual color of the sprite displayed on radar
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(0.1, 0.1, None)

                distance = ((player.x - sprite.x) ** 2 + (player.y - sprite.y) ** 2) ** 0.5
                if distance < player.radar:
                    pen.stamp() # stamps a copy of the turtle shape at the current turtle position
                


# Create the border
game = Game(600, 400)

# Create the radar
radar = Radar(400, -200, 200, 200)

# Creating the player sprite as a spaceship
player = Player(0,0, 'triangle', 'white') # putting the player in the center

# Creating the Camera
camera = Camera(player.x, player.y)

# Creating missile object
missiles = []
for _ in range(3):
    missiles.append(Missile(0, 100, 'circle', 'yellow'))

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

window.onkeypress(game.start, 's')
window.onkeypress(game.start, 'S')

# Main Loop
while True:
    # Splash
    if game.state == 'splash':
        window.update()
    
    elif game.state == 'playing':   
        # Clear the screen
        pen.clear()

        # Update the Sprites to move around the screen
        for sprite in sprites:
            sprite.update()

        # check for collision
        for sprite in sprites:
            if isinstance(sprite, Enemy) and sprite.state == 'active':
                if player.is_collision(sprite):
                    sprite.health -= 10
                    player.health -= 10
                    player.bounce(sprite)

                for missile in missiles:
                    if missile.state == 'active' and missile.is_collision(sprite):
                        sprite.health -= 10
                        missile.reset()

            if isinstance(sprite, Powerup):
                if player.is_collision(sprite):
                    sprite.x = 100
                    sprite.y = 100

                for missile in missiles:
                    if missile.state == 'active' and missile.is_collision(sprite):
                        sprite.x = 100
                        sprite.y = -100
                        missile.reset()


        # Render the Sprites
        for sprite in sprites:
            sprite.render(pen, camera.x + 100, camera.y)

        # Render the borders
        game.render_border(pen, camera.x + 100, camera.y)

        # Check for end of the level
        end_of_level = True
        for sprite in sprites:
            # First look if an enemy sprite is still active
            if isinstance(sprite, Enemy) and sprite.state == 'active':
                end_of_level = False

        if end_of_level:
            game.level += 1
            game.start_level()

        # Updating the camera
        camera.update(player.x, player.y)

        # draw text
        #character_pen.draw_string(pen, '@KARIM', 0, 0)
        game.render_info(pen, 0, 0)

        # Render the radar
        radar.render(pen, sprites)

        # Update the Screen
        window.update()


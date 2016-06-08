# program template for Spaceship
import simplegui
import math
import random

# global constant
DIMENSION = 2
FRICTION = 0.05
VEL_ACC = 0.5
MISSILE_SPEED = 8
CANVAS = [800, 600]
WIDTH = CANVAS[0]
HEIGHT = CANVAS[1]
# fix_angel_vel, vel_acc, is_thrust
fix_angel_vel = 0.03
vel_acc = 0
input_map = {"up":(0, VEL_ACC, 1), "w":(0, VEL_ACC, 1), 
             "left":(-fix_angel_vel, 0, 3), "a":(-fix_angel_vel, 0, 3), 
             "right":(fix_angel_vel, 0, 3), "d":(fix_angel_vel, 0, 3), 
             "down":(0, -.5 * VEL_ACC, 3), "s":(0, -.5 * VEL_ACC, 3)} 

#global variables 
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def start():
    global lives, score, time, started, debris_image, nebula_image
    lives = 3
    score = 0
    time = 0
    timer.start()
    soundtrack.play()
    started = True
    debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
    nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

    
def stop():
    global rock_group, started
    timer.stop()
    rock_group = set([])
    soundtrack.rewind()
    started = False

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(group, canvas):
    for single in set(group):
        single.draw(canvas)
        if single.update():
            group.remove(single)
            
def group_collide(rock_group, single):
    collide = False
    for rock in set(rock_group):
        if rock.collide(single):
            collide = True
            explosion_group.add(Sprite(rock.get_pos(), [0, 0], rock.get_angle(), 0, explosion_image, explosion_info, explosion_sound))
            rock_group.discard(rock)
    return collide

def group_group_collide(rock_group, missile_group):
    score = 0
    for missile in set(missile_group):
        if group_collide(rock_group, missile):
            missile_group.discard(missile)
            score += 1
    return score


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.toward = angle_to_vector(self.angle)
        
    def update_angel(self, fix_angel_vel):
        self.angle_vel += fix_angel_vel
    
    def set_thrust(self, is_thrust):
        if is_thrust == 1:
            self.thrust = True
            ship_thrust_sound.play()
        elif is_thrust == 0:
            self.thrust = False
            ship_thrust_sound.rewind()
    
    def get_angle(self):
        return self.angle
    
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def shoot(self):
        global missile_group
        missile_group.add(Sprite([self.pos[0] + self.image_center[0] * self.toward[0], 
                          self.pos[1] + self.image_center[0] * self.toward[1]], 
                         [self.vel[0] + MISSILE_SPEED * self.toward[0], 
                          self.vel[1] + MISSILE_SPEED * self.toward[1]], 
                          0, 0, missile_image, missile_info, missile_sound)
                          )
    
    def draw(self,canvas):
        canvas.draw_image(self.image, 
                          [self.image_center[0] + self.thrust * self.image_size[0], 
                           self.image_center[1]], 
                          self.image_size, self.pos,self.image_size , self.angle)

    def update(self):
        self.toward = angle_to_vector(self.angle)
        for dim in range(DIMENSION):
            self.vel[dim] = (self.vel[dim] + vel_acc * self.toward[dim]) * (1-FRICTION)
            self.pos[dim] = (self.pos[dim] + self.vel[dim]) % CANVAS[dim]
        self.angle += self.angle_vel
        
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def get_angle(self):
        return self.angle
    
    def collide(self, other):
        return  dist(self.pos,other.get_pos()) < self.radius + other.get_radius()
        
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, 
                              [self.image_center[0] + (self.age % self.lifespan) * self.image_size[0], self.image_center[1]], 
                              self.image_size, self.pos, self.image_size, self.angle)
                              
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, 
                              self.pos, self.image_size, self.angle)
        
    def update(self):
        self.age += 1
        for dim in range(DIMENSION):
            self.pos[dim] = (self.pos[dim] + self.vel[dim]) % CANVAS[dim]
        self.angle += self.angle_vel
        if self.age > self.lifespan:
            return True
        else:
            return False
        
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        start()
           
def draw(canvas):
    global time, lives, score, debris_image, nebula_image
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw user interface
    canvas.draw_text("lives = " + str(lives), [WIDTH / 6, HEIGHT / 10], 
                     22, "White")
    canvas.draw_text("score = " + str(score), [WIDTH * 4 / 6, HEIGHT / 10], 
                     22, "White")
    # draw and update rocks and missiles
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    
    # draw and update ship
    my_ship.draw(canvas)
    my_ship.update()
    
    # update lives if ship collides rock
    if group_collide(rock_group, my_ship):
        lives -= 1
    if lives < 1:
        stop()
        
    # update score
    score += 10 * group_group_collide(rock_group, missile_group)
    if score == 300:
        debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png")
        nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
# key handler
def keydown(key):
    global vel_acc
    for i in input_map:
        if key == simplegui.KEY_MAP[i]:
            my_ship.update_angel(input_map[i][0])
            vel_acc += input_map[i][1]
            my_ship.set_thrust(input_map[i][2])
    if key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
    if key == simplegui.KEY_MAP["q"]:
        pause()
                                             
                                             

def keyup(key):
    global vel_acc
    for i in input_map:
        if key == simplegui.KEY_MAP[i]:
            my_ship.update_angel(-input_map[i][0])
            vel_acc -= input_map[i][1]
            my_ship.set_thrust(input_map[i][2]-1)
        
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len(rock_group) <13 and started:
        random_pos = [WIDTH * random.random(), HEIGHT * random.random()]
        while dist(random_pos, my_ship.get_pos()) < 200:
            random_pos = [WIDTH * random.random(), HEIGHT * random.random()]
        rock_group.add(
                       Sprite(random_pos, 
                       [score / 100.0 * (random.random() - 0.5), score / 100.0 * (random.random() - 0.5)], 
                        2 * math.pi * random.random(), 
                       .1 * (random.random() - 0.5), 
                        asteroid_image, asteroid_info)
                      )
            
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

def pause():
    if timer.is_running():
        timer.stop()
        soundtrack.pause()
    else:
        timer.start()
        soundtrack.play()
    
frame.add_button("Start Game", start, 200)
frame.add_button("Pause Generate Rocks", pause, 200)
frame.add_button("Game Over", stop, 200)


timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

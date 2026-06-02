import pygame
import time
import math
import random
pygame.init() # initialization of pygame module

WIDTH, HEIGHT = 1280, 650 #width and the height of the screen
window = pygame.display.set_mode((WIDTH,HEIGHT)) # defining the window

pygame.display.set_caption("Ring generation Simulation") #setting the caption

# ROCHE_LIMIT = 18400
# EARTH_DIAMETER = 12756
# MOON_DIAMETER = 3475
EARTH_MASS = 5.9722e24
MOON_MASS = 7.34767309e22
FRAGMENT_MASS = 7.346e19
G = 6.6743e-11
FPS = 150
PLANET_SIZE = 3.5
FRAGMENT_SIZE = 1
VEL_SCALE = 100
MOON_SIZE = 1

#defining the vectors
background_image = pygame.transform.scale(pygame.image.load("background.jpg"),(WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("earth.webp"),(PLANET_SIZE * 2, PLANET_SIZE * 2))

#defining the colors in case we need to use them again
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

class Earth:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        
    def draw(self):
        window.blit(PLANET, (self.x-PLANET_SIZE, self.y-PLANET_SIZE))

class Moon_fragment:
    def __init__(self, x, y, x_vel, y_vel, mass):
        # Random point in a circle of radius 35
        theta = random.uniform(0, 2 * math.pi)
        r = (0.9556840075*2) * math.sqrt(random.random())
        self.x = x + r * math.cos(theta)
        self.y = y + r * math.sin(theta)

        #d_a_velx = 35 * math.cos(theta)
        #d_a_vely = 35 * math.sin(theta)

        self.x_vel = x_vel #+ d_a_velx
        self.y_vel = y_vel #+ d_a_vely
        self.mass = mass

    def move(self, planet = None):

        distance = math.sqrt((self.x -planet.x)**2 +(self.y - planet.y)**2) * 1816500

        f = (G * self.mass * planet.mass) / distance ** 2

        acceleration = f / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = (acceleration * math.cos(angle)) 
        acceleration_y = (acceleration * math.sin(angle))

        self.x_vel += (acceleration_x /1816500) * 4
        self.y_vel += (acceleration_y /1816500) * 4

        self.x += (self.x_vel /1816500) * 4
        self.y += (self.y_vel /1816500) * 4

    # def calculate(distance):
    #     if pygame.time.get_ticks() == 0:
    #         print()

    def draw(self):
        pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), FRAGMENT_SIZE)

class Moon:
    def __init__(self, x, y, x_vel, y_vel, mass):
        # Random point in a circle of radius 35
        #theta = random.uniform(0, 2 * math.pi)
        #r = 35 * math.sqrt(random.random())
        self.x = x# + r * math.cos(theta)
        self.y = y# + r * math.sin(theta)

        self.x_vel = x_vel
        self.y_vel = y_vel 
        self.mass = mass

    def move(self, planet = None):

        r = math.sqrt((self.x -planet.x)**2 +(self.y - planet.y)**2) * 1816500
        
        f = (G * self.mass * planet.mass) / r ** 2
        
        acceleration = f / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = (acceleration * math.cos(angle)) 
        acceleration_y = (acceleration * math.sin(angle))
        self.x_vel += (acceleration_x /1816500) * 4
        self.y_vel += (acceleration_y /1816500) * 4

        self.x += (self.x_vel /1816500) * 4
        self.y += (self.y_vel /1816500) * 4

        print(f" Distance = {r} \n Position {self.x},{self.y} \n f = {f} \n Acceleration_x {acceleration_x * 1816500} \n Acceleration_y {acceleration_y * 1816500} \n Velocity_x {self.x_vel/1816500 *2} \n Velocity_y {self.y_vel/1816500*2}\n")
        # print((G * planet.mass)/(r/1816500 *2))

    def draw(self):
        pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), MOON_SIZE)

def create_moon_fragment(coordinates):

    tx, ty = coordinates
    velx = 0
    vely = -798.25
    obj = Moon_fragment(tx, ty, velx, vely, FRAGMENT_MASS)
    return obj

def create_semirealistic_moon(coordinates):
    tx, ty = coordinates
    velx = 0
    vely = -7982.5
    obj = Moon(tx, ty, velx, vely, MOON_MASS)
    return obj

#   the main function that only runs when the file is ran directly
def main():
    on = True # variable to store the information whether the simulation is being ran or not
    clock = pygame.time.Clock() # a clock for keeping track of events and updating the window

    planet = Earth(WIDTH/2, HEIGHT/2, EARTH_MASS)
    objects = [] # array to store the objects
    temp_obj_pos = None #temporary holder of the object that will be spawned in

    while on: # while the simulation is being ran 
        clock.tick(FPS) #sets a limit on the frames per second so the simulation is same for all of the computers that run this code directly

        mouse_position = pygame.mouse.get_pos() #get the mouse position constantly and store it in this variable
        roche_limit_pos = 840,325
         
        #event loop
        for event in pygame.event.get(): # run till you get every event in the pygame module
            if event.type == pygame.QUIT: # if it is this specific event "QUIT"
                on = False #then close simulation
                
            if event.type == pygame.MOUSEBUTTONDOWN: #if a mouse button is pressed
                temp_obj_pos = mouse_position
                for i in range(1001):
                    i + 1
                    obj = create_moon_fragment(temp_obj_pos)
                    objects.append(obj)
                temp_obj_pos = None #temporary object pos holder is now equal to the momentary mouse position during when this event is detected
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                        obj2 = create_semirealistic_moon(roche_limit_pos)
                        objects.append(obj2)
                if event.key == pygame.K_r:
                    for r in range(1001):
                        r + 1
                        obj = create_moon_fragment(roche_limit_pos)
                        objects.append(obj)

    

        # keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     for i in range(1001):
        #         obj2 = create_realistic_fragment(roche_limit_pos)
        #         objects.append(obj2)


        window.blit(background_image, (0,0)) #make the background
        
        if temp_obj_pos:
            pygame.draw.circle(window, WHITE, temp_obj_pos, FRAGMENT_SIZE) # (window, color, coordinates, radius) respectively

        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            # off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y-planet.y)**2) <= PLANET_SIZE or obj.x < -100 or obj.x > 1380 or obj.y < -200 or obj.y > 850
            
            if collided:
                objects.remove(obj)  

        planet.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__": # initialization that only runs the main line of code of the simulation if this file is ran directly
    main()

#  Distance = 363300.0 
#  Position 839.9963427170928,324.11918524635286
#  f = 2.2174646663770926e+26
#  Acceleration_x -3.3217272004015985
#  Acceleration_y 4.067942583612516e-16
#  Velocity_x -0.0036572829071308544
#  Velocity_y -0.8808147536471236
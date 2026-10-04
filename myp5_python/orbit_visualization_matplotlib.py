import math
import matplotlib.pyplot as plt

# t = 0
# dt = 0.1
# p = 0 
# v = 0
# a = 10
G = 1
pm = 65
px = 0
py = 0
sm = 1
sx = 2
sy = 0
svx = 0
svy = 5
t = 0
dt = 0.001


x_points = []
y_points = []

# for i in range(11):
#     print(f"Velocity: {v}")
#     print(f"Acceleration: {a}")
#     print(f"Position: {p}")
#     print(f"Time: {t}\n")
#     v += a * dt
#     p += v * dt
#     t += dt

class attractor:
    def __init__(self, mass, x, y):
        self.mass = mass
        self.x = x
        self.y = y

class orbiter:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def orbit(self):
        i = 0
        while i < 10000:

            r = math.sqrt((px-self.x)**2 + (py-self.y)**2) #Using self here is important otherwise the satellite stays still if global variables are used
            f = (G*pm*sm)/r**2
            theta = math.atan2((py-self.y), (px-self.x)) # This is because self.x and y is updated not the global variables so using them as inputs for acceleration would dumb
            a = f/sm

            ax = a*math.cos(theta)
            ay = a*math.sin(theta)

            self.vx += ax * dt
            self.vy += ay * dt

            self.x += self.vx * dt
            self.y += self.vy * dt

            x_points.append(self.x)
            y_points.append(self.y)
            i += 1

            
        

satellite = orbiter(sm, sx, sy, svx, svy)
planet = attractor(pm, px, py)

satellite.orbit()

plt.figure(figsize=(6,6))
plt.plot(x_points, y_points, label="Satellite trajectory", color= "blue")
plt.scatter(0, 0, color='red', s=100, label= "Stationary planet")

plt.axis('equal')
plt.title("2D satellite trajectory calculation simulation")
plt.xlabel("x position")
plt.ylabel("y position")
plt.show()

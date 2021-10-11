import pygame
from coms import *
from graph import *
from colors import *
from math import *

# недоделано
FPS = 120
WIDTH = 1100  # ширина экрана
HEIGHT = 700  # высота экрана
spd = 10  # скорость передвижения экрана
x_spd = 0
y_spd = 0
x_delta = 0
y_delta = 0
dq = 1
qr = 1.05

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

time = 0
Forces = []
Bodies = []

# __input here your main code______________________________________

q = 0.2  # start scale
сheck = True

Bodies.append(Body(r=3, m=10, c=3))
Bodies.append(Body(x=2300, r=3, m=10, spy=0, c=3))
# Bodies.append(Body())

# __end_____________________________________________________________

for i in Bodies:
    Forces.append(GForce(i))
    Forces.append(EForce(i))

while 1:
    sc.fill(GRAY())
    # print(x_spd, y_spd)
    time += 1
    x_delta += x_spd
    y_delta += y_spd
    q *= dq

    for i in range(len(Bodies)):
        for j in range(i + 1, len(Bodies)):
            collide(Bodies[j], Bodies[i])

    for i in Bodies:
        pygame.draw.circle(sc, KINOVAR(),
                           (trans(HEIGHT, WIDTH, HEIGHT, WIDTH,
                                  [(i.x - x_delta) * q, (i.y - y_delta) * q])),
                           i.radius)

        i.move_trd()
        i.react(Forces)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x_spd = -spd / q
            elif i.key == pygame.K_RIGHT:
                x_spd = spd / q
            elif i.key == pygame.K_UP:
                y_spd = spd / q
            elif i.key == pygame.K_DOWN:
                y_spd = -spd / q
            elif i.key == pygame.K_m:
                dq = qr
            elif i.key == pygame.K_n:
                dq = 1 / qr
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                x_spd = 0
            elif i.key in [pygame.K_DOWN, pygame.K_UP]:
                y_spd = 0
            elif i.key in [pygame.K_n, pygame.K_m]:
                dq = 1

    pygame.display.update()

    clock.tick(FPS)

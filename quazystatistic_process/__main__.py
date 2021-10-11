import pygame
from __coms__ import *
from GraphComs import *
from __Colors__ import *
from math import *

# недоделано
FPS = 50
WIDTH = 1100  # ширина экрана
HEIGHT = 700  # высота экрана
BoxWIDTH = WIDTH // 2  # ширина
BoxHEIGHT = HEIGHT  # высота
MaxPressure = 100  # ля графика
MaxValue = 40

Quantity = 100
Maxspeed = 5
Xmax = BoxWIDTH / 2
Ymax = BoxHEIGHT / 2
MoleculasRD = []
MoleculasLD = []
MoleculasRU = []
MoleculasLU = []


Walls = []
elspeed = 2
betspeed = 4
time = 0
Graph = []

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

for i in range(Quantity):
    MoleculasRD.append(Corpuscula(Maxspeed, Xmax, 0, 0, -Ymax))

for i in range(Quantity):
    MoleculasLD.append(Corpuscula(Maxspeed, 0, 0, -Xmax, -Ymax))

for i in range(Quantity):
    MoleculasRU.append(Corpuscula(Maxspeed, Xmax, Ymax, 0, 0))

for i in range(Quantity):
    MoleculasLU.append(Corpuscula(Maxspeed, 0, Ymax, -Xmax, 0))

Walls.append(Wall(Xmax, Ymax, Xmax, -Ymax, 90, 0))  # right
Walls.append(Wall(-Xmax, Ymax, -Xmax, -Ymax, 90, 0))  # left
Walls.append(Wall(-Xmax, -Ymax, Xmax, -Ymax, 0, 0))  # down
Walls.append(Wall(-Xmax, Ymax, Xmax, Ymax, 0, 0))  # up
Walls.append(Wall(0, Ymax, 0, -Ymax, 90, 0))
Walls.append(Wall(-Xmax, 0, Xmax, 0, 0, 0))
GraphColors = [SKYBLUE(), WHITE(), KINOVAR(), BERLIN_LAZUR(), LUMINESCENTRED()]

Moleculas = MoleculasLD + MoleculasRD + MoleculasLU + MoleculasRU

while 1:
    sc.fill(GRAY())

    for i in range(len(Graph)):

        pygame.draw.circle(sc, GraphColors[i%3], Graph[i], 1, 1)

    time += 1

    Temperature = sum([(i.speedx ** 2 + i.speedy ** 2) for i in Moleculas]) / 2 /Quantity
    Value = abs((Walls[0].x0 - Walls[1].x0) * (Walls[0].y0 - Walls[0].y1)) / 10000
    if Value!=0:
        Pressure = Temperature / Value

    TemperatureLD = sum([(i.speedx ** 2 + i.speedy ** 2) for i in MoleculasLD]) / Quantity
    ValueLD = abs((Walls[4].x0 - Walls[1].x0) * (Walls[0].y0 - Walls[0].y1)) / 10000
    if ValueLD != 0:
        PressureLD = TemperatureLD / ValueLD

    TemperatureRD = sum([(i.speedx ** 2 + i.speedy ** 2) for i in MoleculasRD]) / Quantity
    ValueRD = abs((Walls[0].x0 - Walls[4].x0) * (Walls[0].y0 - Walls[0].y1)) / 10000
    if ValueRD != 0:
        PressureRD = TemperatureRD / ValueRD

    TemperatureLU = sum([(i.speedx ** 2 + i.speedy ** 2) for i in MoleculasLU]) / Quantity
    ValueLU = abs((Walls[4].x0 - Walls[1].x0) * (Walls[0].y0 - Walls[0].y1)) / 10000
    if ValueLU != 0:
        PressureLU = TemperatureLU / ValueLU

    TemperatureRU = sum([(i.speedx ** 2 + i.speedy ** 2) for i in MoleculasRU]) / Quantity
    ValueRU = abs((Walls[0].x0 - Walls[4].x0) * (Walls[0].y0 - Walls[0].y1)) / 10000
    if ValueRU != 0:
        PressureRU = TemperatureRU / ValueRU
    # print(round(Pressure,3), round(Value, 3), round(Temperature, 3) )

    if time % 1 == 0:
        Graph.append([int(Value / MaxValue * (WIDTH - BoxWIDTH)), int(HEIGHT - Pressure / MaxPressure * HEIGHT)])
        Graph.append([int(ValueLD / MaxValue * (WIDTH - BoxWIDTH)), int(HEIGHT - PressureLD / MaxPressure * HEIGHT)])
        Graph.append([int(ValueRD / MaxValue * (WIDTH - BoxWIDTH)), int(HEIGHT - PressureRD / MaxPressure * HEIGHT)])
        Graph.append([int(ValueLU / MaxValue * (WIDTH - BoxWIDTH)), int(HEIGHT - PressureLU / MaxPressure * HEIGHT)])
        Graph.append([int(ValueRU / MaxValue * (WIDTH - BoxWIDTH)), int(HEIGHT - PressureRU / MaxPressure * HEIGHT)])


    for i in MoleculasRD:
        pygame.draw.circle(sc, KINOVAR(), (trans(HEIGHT, WIDTH, BoxHEIGHT, BoxWIDTH, [i.x, i.y])), 2)

    for i in MoleculasLD:
        pygame.draw.circle(sc, WHITE(), (trans(HEIGHT, WIDTH, BoxHEIGHT, BoxWIDTH, [i.x, i.y])), 2)

    for i in MoleculasRU:
        pygame.draw.circle(sc, BERLIN_LAZUR(), (trans(HEIGHT, WIDTH, BoxHEIGHT, BoxWIDTH, [i.x, i.y])), 2)

    for i in MoleculasLU:
        pygame.draw.circle(sc, LUMINESCENTRED(), (trans(HEIGHT, WIDTH, BoxHEIGHT, BoxWIDTH, [i.x, i.y])), 2)

    for i in Walls:
        Coordins = [trans(HEIGHT, WIDTH, BoxHEIGHT, BoxWIDTH, j) for j in i.coords()]
        pygame.draw.line(sc, BLACK(), Coordins[0], Coordins[1])


    deltaPressureV = PressureLD + PressureLU - PressureRD - PressureRU

    if deltaPressureV>0:
        Walls[4].speed = betspeed/10
    elif deltaPressureV<0:
        Walls[4].speed = -betspeed / 10
    else:
        Walls[4].speed = 0

    deltaPressureG = PressureLD - PressureLU + PressureRD - PressureRU

    if deltaPressureG > 0:
        Walls[5].speed = betspeed / 10
    elif deltaPressureG < 0:
        Walls[5].speed = -betspeed / 10
    else:
        Walls[5].speed = 0

    pygame.display.update()

    for i in Moleculas:

        for j in Walls:
            i.trycolli(j)
        '''
        if abs(i.x + i.speedx) >= BoxWIDTH/2:
            i.speedx *= -1
        if abs(i.y + i.speedy) >= BoxHEIGHT/2:
            i.speedy *= -1'''
        i.move()

        i.clocktickes()

    for i in Walls:
        i.move()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                Walls[1].speed = -elspeed
            elif i.key == pygame.K_RIGHT:
                Walls[1].speed = elspeed
            elif i.key == pygame.K_UP:
                Walls[2].speed = elspeed
            elif i.key == pygame.K_DOWN:
                Walls[2].speed = -elspeed
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                Walls[1].speed = 0
            elif i.key in [pygame.K_DOWN, pygame.K_UP]:
                Walls[2].speed = 0
        # elif i.type == pygame.MOUSEBUTTONDOWN:
        #    if i.button == 1:

    print('___________________________')
    print(round(Pressure,3), round(Value,3), round(Temperature,3))
    print(round(PressureLD, 3), round(ValueLD, 3), round(TemperatureLD, 3))
    print(round(PressureRD, 3), round(ValueRD, 3), round(TemperatureRD, 3))
    print(round(PressureLU, 3), round(ValueLU, 3), round(TemperatureLU, 3))
    print(round(PressureRU, 3), round(ValueRU, 3), round(TemperatureRU, 3))

    clock.tick(FPS)

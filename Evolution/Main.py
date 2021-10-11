from pygame import *
from random import *
from math import *


def f(x):
     #return -0.2*x**4 - 0*x**3 + 2.2*x**2 + 0.5*x +1
    # return -3.1*x**6 -0.1*x**5 + 7.4 *x**4 - 0.1 *x**3 - 1.8*x**2 + 0.3*x + 1
    return 10 * (sin(x))


def coo(x, y):
    y *= 20
    x *= 40

    x += 500
    y = -y + 250

    x = int(x)
    y = int(y)

    return (x, y)

stp = False

FPS = 30
WIN_WIDTH = 1000
WIN_HEIGHT = 500

BLUE = (27, 42, 207)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (250, 150, 100)
GREEN = (57, 255, 20)
RED = (255, 0, 0)

Q = 200
MQ = 0
UQ = []
users = []
users1 = []
mid = []
# users = [1, 2.5, 3, -5, 10, -9, -4, 1, -3, -7, -10,  -15, -11, -9.8, -9, 5]
# users = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#users = [4.525, -2.45, 12.425, -9.25, -5.3, -2.35, -7.55, -8.2, 9.3, -2.175, 3.3, 1.425, 3.15, 6.575, -5.45, -4.35, 0.55, 12.025, -0.475, 7.35, -11.575, -9.024999999999999, -0.125, 2.875, 9.45, -0.25, -6.375, 3.825, 12.25, 6.8, 12.25, 4.075, 7.375, -12.425, -4.95, 7.1125, 1.7125000000000001, 6.8375, -6.9625, 4.2375, 3.5125, 3.475, 0.6875000000000002, 5.975, 12.2125, 7.800000000000001]
# for i in range(20):
#    users.append(1)
for i in range(500):
    a = (randrange(1000) - 500) / 40
    users.append(a)
init()

clock = time.Clock()
sc = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
print(MQ, len(users), users)

while 1:
    RED = (255, MQ%256, 255 - MQ%256)
    sc.fill(WHITE)
    MQ += 1
    for i in event.get():
        if i.type == QUIT: exit()
    z = False
    for x in range(-1000, 1001):
        # x-=500
        x = float(x)
        x /= 40
        y = f(x)

        x, y = coo(x, y)

        # print('2')
        if (z):
            # print('0')
            if (0 <= x <= 1000) and (0 <= y <= 500):
                draw.line(sc, BLACK, (x1, y1), (x, y))

        # draw.circle(sc, BLACK, (x, y), 1)
        x1, y1 = x, y
        z = True

    draw.line(sc, ORANGE, (0, 250), (1000, 250))
    draw.line(sc, ORANGE, (500, 0), (500, 500))

    qqq = True
    if ((not stp)  or True) and len(users)!=0:
        # размножение
        l = len(users)
        for i in range(3 *l//5 ):
            a1 = randrange(l)
            a2 = randrange(l)
            users.append((users[a1] + users[a2]) / 2)
            #users.append((users[a1] - users[a2])/2)
            '''
            if users[a1]!=-users[a2]:
                
                # a=((users[a1] + users[a2]) / 2)
                # a = ((users[a1] - users[a2])/2)
                # a = ((users[a2]+users[a1])/abs(users[a2]+users[a1])*sqrt(users[a1]**2 + users[a2]**2) )
               # a = ((users[a2] + users[a1]) / abs(users[a2] + users[a1]) * sqrt(abs(users[a1] ** 2 - users[a2] ** 2)))
                 a = ((users[a2] + users[a1]) / abs(users[a2] + users[a1]) * sqrt(abs(users[a2]*users[a1])))
            else:
                q = randrange(2) - 1
                #a = q *sqrt(abs(users[a1] ** 2 - users[a2] ** 2))

            users.append(a)'''

        # мутации
        l = len(users)
        for i in range(l // 5):
            a1 = randrange(l)
            # a2 = randrange(21)/10 - 1
            a2 = randrange(6) / 10 - 0.25
            users[a1] += a2

        # сражения
        l = len(users)
        for i in range(l // 3 ):
            a1 = randrange(l)
            a2 = randrange(l)
            l -= 1
            if (f(users[a1]) > f(users[a2])):
                del users[a2]
            elif (f(users[a1]) < f(users[a2])):
                del users[a1]

        # внезапная смерть
        l = len(users)
        a = randrange(l)
        del users[a]
        for i in range(l//10):
            l = len(users)
            a = randrange(l)
            del users[a]
        print(MQ, len(users), users)

    for i in range(len(users)):
        x = users[i]
        y = f(x)
        draw.circle(sc, RED, coo(x, y), 3, 2)

    if (len(users)!=0):
        x0 = sum(users) / len(users)
        y0 = sum([f(x) for x in users]) / len(users)
        mid.append(coo(x0,y0))

        if (MQ <= Q):
            UQ.append(len(users))
        else:
            if (UQ[0] == len(users)) and (max(users) - min(users) <= 1):
                stp = True
            else:
                for i in range(Q - 1):
                    UQ[i] = UQ[i + 1]
                UQ[Q - 1] = len(users)

    else:
        draw.line(sc, BLUE, (0,0), (1000, 500), 3)
        draw.line(sc, BLACK, (6, 0), (1006, 500), 6)
        draw.line(sc, BLACK, (-6, 0), (994, 500), 6)

    for i in range(len(mid)):
        if (i!=0):
            draw.line(sc, GREEN, mid[i-1], mid[i])




    display.update()

    clock.tick(FPS)
































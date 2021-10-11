from pygame import *
from random import *
from math import *


class User():
    global upper
    global veroyatnostpola

    veroyatnostpola = 10
    upper = 1
    maxwell = 10
    maxreproduction = 3
    maxmutation = 1
    gender = 0

    value = 0
    reprodaction = 1

    def neu(self):
        self.value = (randrange(2 * self.maxwell * 100 + 1)) / 100 - self.maxwell
        self.reprodaction = randrange(self.maxreproduction)
        self.gender = randrange(2000)%2

    def define(self, val, rep):
        self.value = val
        self.reprodaction = rep
        self.gender = randrange(2000)%2

    def reproduct(self, Username):
        Newfags = []
        Quan = round((self.reprodaction + Username.reprodaction) / 2)

        for i in range(Quan):
            NewUser = User()
            NewValue = (self.value + Username.value) / 2
            NewReprodaction = (self.reprodaction + Username.reprodaction) / 2
            NewUser.define(NewValue, NewReprodaction)
            if self.gender == Username.gender:
                NewUser.gender = self.gender
            Newfags.append(NewUser)

        return [Quan, Newfags]

    def mutate(self):
        a = (randrange(veroyatnostpola))

        if (a <veroyatnostpola//2):
            Delta = (randrange(self.maxmutation * 2 * 100 + 1)) / 100 - self.maxmutation
            self.value += Delta
        elif (a<veroyatnostpola-1):
            Delta = randrange(3) - 1
            self.reprodaction += Delta
            if (self.reprodaction > self.maxreproduction + upper or self.reprodaction < 0):
                self.reprodaction -= Delta
        else:
            self.gender = int(not (bool(self.gender)))


def f(x):
    # return -0.2*x**4 - 0*x**3 + 2.2*x**2 + 0.5*x +1
    # return -3.1*x**6 -0.1*x**5 + 7.4 *x**4 - 0.1 *x**3 - 1.8*x**2 + 0.3*x + 1
    x = abs(x)
    if 2**(2/3)-x**(2/3)>0:
        boom = [(2**(2/3)-x**(2/3))**(3/2), -(2**(2/3)-x**(2/3))**(3/2)]
    else:
        boom = [0, 0]
    #print(boom)
    return boom


def coo(x, y):
    y *= 120
    x *= 120
    #x-=50

    x += 500
    y = -y + 250

    x = int(x)
    y = int(y)

    return (x, y)


stp = False

FPS = 2
WIN_WIDTH = 1000
WIN_HEIGHT = 500

BLUE = (27, 42, 207)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (250, 150, 100)
GREEN = (57, 255, 20)
RED = (255, 0, 0)


init()

clock = time.Clock()
sc = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

while 1:
    sc.fill(WHITE)
    for i in event.get():
        if i.type == QUIT: exit()

    for ttt in range(len(f(0))):
        z = False
        for x in range(-1000, 1001):
            # x-=500
            x = float(x)
            x /= 40
            y = f(x)[ttt]
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

    display.update()

    clock.tick(FPS)

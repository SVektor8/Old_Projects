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
    return 10 * (sin(x))


def coo(x, y):
    y *= 20
    x *= 120
    x-=50

    x += 500
    y = -y + 250

    x = int(x)
    y = int(y)

    return (x, y)


stp = False

FPS = 1500
WIN_WIDTH = 1000
WIN_HEIGHT = 500

BLUE = (27, 42, 207)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (250, 150, 100)
GREEN = (57, 255, 20)
RED = (255, 0, 0)

radius = 3
tolshina = 1
UsersQuantity = 50
ReproductionC = 3 / 4
SuddenDeathC = 1 / 8
MutationC = 1 / 5
BattleC = 1 / 4

Q = 200
MQ = 0
UQ = []
users = []
users1 = []
mid = []

for i in range(UsersQuantity):
    NewUser = User()
    NewUser.neu()
    users.append(NewUser)

init()

clock = time.Clock()
sc = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
print(MQ, len(users), users)

while 1:
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
    if ((not stp) or True) and len(users) != 0:
        # размножение
        l = len(users)
        for i in range(l // 3):
            a1 = randrange(l)
            a2 = randrange(l)
            res = users[a1].reproduct(users[a2])
            if res[0] != 0:
                for username in res[1]:
                    users.append(username)

        # мутации
        l = len(users)
        for i in range(round(l * ReproductionC)):
            a1 = randrange(l)
            users[a1].mutate()

        # сражения
        l = len(users)
        for i in range(round(l * BattleC)):
            a1 = randrange(l)
            a2 = randrange(l)
            l -= 1
            if (f(users[a1].value) > f(users[a2].value)):
                del users[a2]
            elif (f(users[a1].value) < f(users[a2].value)):
                del users[a1]

        # внезапная смерть
        l = len(users)
        a = randrange(l)
        del users[a]
        for i in range(round(l * SuddenDeathC + l * SuddenDeathC * (l // 100))):
            l = len(users)
            a = randrange(l)
            del users[a]
        print(MQ, len(users), users)

    for i in range(len(users)):
        x = users[i].value
        y = f(x)
        MMM = users[i].reprodaction / (users[i].maxreproduction + upper) * 255
        draw.circle(sc, (255 - users[i].gender*127, MMM, 255 - MMM), coo(x, y), radius, tolshina)

    '''if (len(users) != 0):
        x0 = sum(users) / len(users)
        y0 = sum([f(x) for x in users]) / len(users)
        mid.append(coo(x0, y0))

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
        draw.line(sc, BLUE, (0, 0), (1000, 500), 3)
        draw.line(sc, BLACK, (6, 0), (1006, 500), 6)
        draw.line(sc, BLACK, (-6, 0), (994, 500), 6)

    for i in range(len(mid)):
        if (i != 0):
            draw.line(sc, GREEN, mid[i - 1], mid[i])'''

    display.update()

    clock.tick(FPS)

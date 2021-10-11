from math import *
from graph import *


class Body:  # some body
    mass = 0
    radius = 0
    charge = 0
    speed_x = 0
    speed_y = 0
    acceleration_x = 0
    acceleration_y = 0
    x = 0
    y = 0
    elasticity = 1

    def __init__(self, x=0, y=0, r=0, m=0, c=0, spx=0, spy=0, elastic=1):
        self.mass = m
        self.radius = r
        self.charge = c
        self.x = x
        self.y = y
        self.speed_y = spy
        self.speed_x = spx
        self.elasticity = elastic

    def def_speed(self, spx=0, spy=0):  # define speed
        self.speed_y = spy
        self.speed_x = spx

    def def_acceleration(self, acx=0, acy=0):  # define acceleration
        self.acceleration_x = acx
        self.acceleration_y = acy

    def def_movement(self, spx=0, spy=0, acx=0, acy=0):  # define speed and acceleration
        self.def_speed(spx, spy)
        self.def_acceleration(acx, acy)

    def move_trd(self):  # moves the body due to speed and acceleration
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x += self.acceleration_x
        self.speed_y += self.acceleration_y

    def react(self, *forces):  # recounts acceleration of the body due to list of forces
        self.acceleration_x = 0
        self.acceleration_y = 0

        for force in forces[0]:
            if force.type == 'Gravity':
                force.upd()
                sqr_distance = \
                    round(((self.x - force.x) ** 2 + (self.y - force.y) ** 2), 5)

                if round(sqr_distance, 5) != 0:
                    module = force.coefficient / sqr_distance
                    self.acceleration_x += \
                        - module * (self.x - force.x) / sqrt(sqr_distance)
                    self.acceleration_y += \
                        - module * (self.y - force.y) / sqrt(sqr_distance)

            elif force.type == 'Electric':
                force.upd()
                sqr_distance = \
                    round(((self.x - force.x) ** 2 + (self.y - force.y) ** 2), 5)

                if round(sqr_distance, 5) != 0:
                    module = force.coefficient / sqr_distance * self.charge / self.mass
                    self.acceleration_x += \
                        module * (self.x - force.x) / sqrt(sqr_distance)
                    self.acceleration_y += \
                        module * (self.y - force.y) / sqrt(sqr_distance)


            elif force.type == 'Field':

                self.acceleration_x += force.module * cos(force.alpha)
                self.acceleration_y += force.module * sin(force.alpha)


class Force:
    G = 1000
    K = 1000
    module = 0
    alpha = 0
    type = 'None'

    def __init__(self):
        self.type = 'None'


class GForce(Force):
    x = 0
    y = 0

    def __init__(self, body):
        super().__init__()
        self.body = body
        self.coefficient = self.G * self.body.mass
        self.type = 'Gravity'
        self.x = self.body.x
        self.y = self.body.y

    def upd(self):
        self.coefficient = self.G * self.body.mass
        self.type = 'Gravity'
        self.x = self.body.x
        self.y = self.body.y


class EForce(Force):
    x = 0
    y = 0

    def __init__(self, body):
        super().__init__()
        self.coefficient = self.K * body.charge
        self.type = 'Electric'
        self.x = body.x
        self.y = body.y
        self.body = body

    def upd(self):
        self.coefficient = self.K * self.body.charge
        self.type = 'Electric'
        self.x = self.body.x
        self.y = self.body.y


class FForce(Force):

    def __init__(self, m, a, a_type='radians'):
        super().__init__()
        self.type = 'Field'
        self.module = m
        if a_type == 'degrees':
            a = radians(a)
        self.alpha = a

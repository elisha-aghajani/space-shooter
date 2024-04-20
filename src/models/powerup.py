import random

from src.data import *

class Powerup:

    def __init__(self):
        self.x = random.randrange(WIDTH)
        self.y = 0
        self.speed = POWERUP_SPEED

    def update(self):
        self.y -= self.speed


class HealthPowerup(Powerup):
    pass


class GunPowerup(Powerup):
    pass


class NukePowerup(Powerup):
    pass
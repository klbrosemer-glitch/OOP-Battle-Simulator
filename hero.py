import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 20
        self.defense = 5

    def attack(self):
        passedCritCheck=random.random(1,6) == 6 
        if passedCritCheck:
            return random.randint(1, self.attack_power) * 1.25
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        # Subtract damage, but do not allow health to fall below 0.
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


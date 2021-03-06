class Enemy(object):

    # prefixing the attribute names with underscore ('_')
    # this is not required, but here it is done to prevent modifying them directly from 'main' for example
    def __init__(self, name="Enemy", lives=1, hit_points=0):
        self._name = name
        self._hit_points = hit_points
        self._init_hit_points = hit_points  # preserving the original points, to reset to them when a life is lost
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
                self._hit_points = self._init_hit_points  # reset the hit_points for the next life if it is not 0
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):  # inherits (extends) the 'Enemy' class

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):  # vampires can 'doge' a hit, by exercising abilities like super-speed :-).
        import random  # This should be added to the top to be used from others. It is here just to show that it can
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges".format(self))
            return True
        else:
            return False

    # overriding the 'take_damage' method (this is NOT overloading. Python do NOT have 'overloading')
    # this is only for vampires, if they do NOT 'dodge"
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)  # if the vampire do not dodge, use the superclass version of 'take_damage"

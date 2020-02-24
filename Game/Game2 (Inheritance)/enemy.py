# class Enemy:  # ... This is to be a "Superclass" from which the other classes will inherit
class Enemy(object):  # ... the same as the above, because classes always inherit the main 'object' class
    # Adding 'object' inside parenthesis is not required for Python 3, it is usr for information

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):  # inherits (extends) the 'Enemy' class

    def __init__(self, name):
        # Prefix with the superclass name (still produces and error if more parameters (except the name) are specified from main)
        # Creating this 'init' method makes it so the 'Enemy' init method (constructor) is not called anymore
        # ... this way of inheritance is the only one available in Python 2
        # # # # Enemy.__init__(self, name=name, lives=1, hit_points=23)

        # the way used in Python 3:
        # # # super(Troll, self).__init__(name=name, lives=1, hit_points=23)

        # OR (preferred):
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))


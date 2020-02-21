class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # hide the 'lives' data attribute by adding underscore. Then the attribute can be only specifically access by asking for " _lives"
        self._level = 1
        self._score = 0

    # "getter" and "setter" for the '_lives' attribute
    def _get_lives(self):  # with the '_' (_lives) if a 'getter' is not created, '_values' will become not displayable ( ... password attribute use-case maybe... )
        return self._lives

    def _set_lives(self, lives):  # with the '_' (_lives) if a 'setter' is not created, '_values' will become read-only (not 'changeable")
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    # "getter" and "setter" for the '_level' attribute
    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000  # increase the score with 100 for every level
            self._level = level
        else:
            print("Level can't be less than 1")

    # properties:

    lives = property(_get_lives, _set_lives)  # the property (lives) should not be the same name as the data attribute (_lives)
    # the "getter" and "setter" inside te parenthesis are called ONLY by name... no '()', to avoid executing the actual methods
    # lives = property(_set_lives, _get_lives)  # Ctrl + click on "property" to see the definition. ("setters" and "getters" cannot be reversed)

    level = property(_get_level, _set_level)  # .. the same rules as for the property 'lives'

    # Alternative syntax for properties ( + ..getters and setters) using 'decorators' (nothing to be gained by converting 'score' to a property, but it shows an alternative syntax
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    # @score.getter           # 'getter' that is not really needed in this case.
    # def score(self):
    #     return self._score

    # # # URL with more information about properties in Python:
    # https://docs.python.org/3/library/functions.html#property
    ###########################################################


    def __str__(self):
        # return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, score {0.score}".format(self)

        # NOTE: The one below is the same as the one above, but a lot less readable.
        return "Name: {0}, Lives: {1}, Level: {2}, score {3}".format(self.name, self.lives, self.level, self.score)

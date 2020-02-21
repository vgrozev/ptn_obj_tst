class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # hide the 'lives' data attribute by adding underscore. Then the attribute can be only specifically access by asking for " _lives"
        self.level = 1
        self.score = 0

    def _get_lives(self):           # with the '_' (_lives) if a 'getter' is not created, '_values' will become not displayable ( ... password attribute use-case maybe... )
        return self._lives

    def _set_lives(self, lives):    # with the '_' (_lives) if a 'setter' is not created, '_values' will become read-only (not 'changeable")
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be ngative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)  # the property (lives) should not be the same name as the data attribute (_lives)

    # the "getter" and "setter" inside te parenthesis are called ONLY by name... no '()', to avoid executing the actual methods
    # lives = property(_set_lives, _get_lives)  # Ctrl + click on "property" to see the definition. ("setters" and "getters" cannot be reversed)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, score {0.score}".format(self)

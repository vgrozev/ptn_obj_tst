# import player
from player import Player

# tim = player.Player("Tim")
tim = Player("Tim")


print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

# import player
from player import Player

# tim = player.Player("Tim")
tim = Player("Tim")

print(tim.name)
print(tim.lives)

# decrease lives
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

# increase lives
tim.lives = 9
print(tim)

# increase levels
tim.level = 2
print(tim)

tim.level += 5
print(tim)

# decrease levels
tim.level = 3
print(tim)

tim.level -= 5
print(tim)

# change score
tim.score = 500
print(tim)


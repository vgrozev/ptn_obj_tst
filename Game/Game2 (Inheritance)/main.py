from enemy import Enemy, Troll  # the Troll imports two classes

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# the one below is failing because 'Enemy' does not have the method 'grunt'
# # monster = Enemy("Basic enemy")
# # monster.grunt()



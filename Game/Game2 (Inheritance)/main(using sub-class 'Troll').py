from enemy import Enemy, Troll      # the Troll imports two classes

ugly_troll = Troll()                # the Troll constructor takes 0 arguments (Hit points 0 (default), Lives: 1 (default))
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)  # the Troll constructor takes 3 arguments (Hit points 18 (provided), Lives: 1 (provided))
print("Another troll - {}".format(another_troll))

brother = Troll("Urg", 23)          # the Troll constructor takes 2 arguments (Hit points 23 (provided), Lives: 1 (default))
print(brother)

"""
    What is going on above id NOT 'method overloading', because Python does not have that concept.
    In this case, since the 'brother' object is created last, it will be the only one that actually exists
    This approach works if '__init()__' method is not yet created in the 'Troll' class
"""

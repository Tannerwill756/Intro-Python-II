# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room="outside"):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"<Welcome, {self.name}! You're in the {self.current_room} room>"


def input_f():
    return input("Would you like to go north, south, east or west? ")


def outside(room, user):
    result = input_f()
    result.lower()
    if result[0] == "n":
        player = Player(user, "foyer")
        print(f"You have now entered the {player.current_room} Room")

    else:
        print("You can only go north out of this room.")
        outside(room, user)


"""
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
"""

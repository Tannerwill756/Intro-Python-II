# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, logged_in=False):
        self.name = name
        self.current_room = current_room
        self.logged_in = logged_in

    def __str__(self):
        return f"<Welcome, {self.name}! You're in the {self.current_room} room>"


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

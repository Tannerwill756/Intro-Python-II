from room import Room
from player import *
import sys
import textwrap
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def input_f():
    return input("Would you like to go north, south, east or west? ")


username = input("Please provide a name for your character: ")
player = Player(username, logged_in=False)


def outside_room():
    if player.current_room == "outside":
        print("You're currently located: " + room["outside"].name + "!")
        print(room["outside"].description)
        direction = input_f().lower()
        if direction[0] == "n":
            player.current_room = "foyer"
            print("You move to the " + player.current_room)
            foyer_room()
        else:
            print("uh oh ")
    else:
        print("uh oh ")


def foyer_room():
    if player.current_room == "foyer":
        print("Your character has arrived to the room: " +
              room["foyer"].name + "!")
        print(room["foyer"].description)
    else:
        print("uh oh ")


def intro():
    print(f"Welcome {username}, let the adventure begin.")
    player.logged_in = True
    if player.logged_in == True:
        outside_room()
    else:
        print("uh oh ")


intro()

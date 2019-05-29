from textwrap3 import wrap
from room import Room
from player import Player

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
c_room = room['outside']
p1 = Player("Player 1", c_room)


# def move(dir, current_room):
#     attribute = dir + '_to'
#     if hasattr(current_room, attribute):
#         return getattr(current_room, attribute)
#     else:
#         print('you can not go that way')

# Write a loop that:
#
while True:
    #     # * Prints the current room name
    #     print(room[p1.current_room].name)
    print(c_room.name)
#     # * Prints the current description (the textwrap module might be useful here).
    lines = wrap(c_room.description, 100)
    for line in lines:
        print(line)
#     # * Waits for user input and decides what to do.
    direction = input("Choose a direction: ")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if direction == 'e':
        if hasattr(c_room, 'e_to'):
            c_room = c_room.e_to
        else:
            print("Can't move East")
    if direction == 'w':
        if hasattr(c_room, 'w_to'):
            c_room = c_room.w_to
        else:
            print("Can't move West")
    if direction == 'n':
        if hasattr(c_room, 'n_to'):
            c_room = c_room.n_to
        else:
            print("Can't move North")
    if direction == 's':
        if hasattr(c_room, 's_to'):
            c_room = c_room.s_to
        else:
            print("Can't move South")
# If the user enters "q", quit the game.
    if direction == 'q':
        print("Bye!")
        break

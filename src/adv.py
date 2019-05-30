from textwrap3 import wrap
from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Rock", "It's just a rock")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Map", "It's an old map, very hard to read")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[ Item("Rope", "Can be used to climb, if you have the skill"), Item("Doge", "Just a cool dog")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Old moldy chest', "There's treasure inside. TREASURE!")]),
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
p1 = Player("Player 1", c_room, [Item("Water", "You know, to drink")])

# Write a loop that:
#

print("\n\n*********************************************")
print("***********  WELCOME TO THE GAME  ***********")
print("*********************************************\n")

while True:
    #     # * Prints the current room name
    print("\n" + c_room.name)
#     # * Prints the current description (the textwrap module might be useful here).
    lines = wrap(c_room.description, 100)
    for line in lines:
        print(line)

    if hasattr(c_room, 'items'):
            for item in c_room.items:
                print(
                    f'Room contains: {item.name}\n')
#     # * Waits for user input and decides what to do.
    direction = input("\nChoose what to do: ")
    more = direction.split(' ')
    if len(more) == 2:
        if more[0] == 'get': 
            inames = [i.name for i in c_room.items]
            if more[1] in inames:
                index = inames.index(more[1])
                item = c_room.items[index]
                c_room.items.remove(item)
                p1.items.append(item)
                item.on_get()
                print(f"{p1.name} now has new item: {item.name}\n")
            else:
                print(f"Current room doesn't hold item {more[1]}\n")
        if more[0] == 'drop':
            inames = [i.name for i in p1.items]
            if more[1] in inames:
                index = inames.index(more[1])
                item = p1.items[index]
                p1.items.remove(item)
                item.on_drop()
                c_room.items.append(item)
                print(f"{c_room.name} now has new item: {item.name}\n")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if direction == 'e':
        if hasattr(c_room, 'e_to'):
            c_room = c_room.e_to
            print("Going East!")
        else:
            print("Can't move East\n")
    if direction == 'w':
        if hasattr(c_room, 'w_to'):
            c_room = c_room.w_to
            print("Going West!")
        else:
            print("Can't move West\n")
    if direction == 'n':
        if hasattr(c_room, 'n_to'):
            c_room = c_room.n_to
            print( "Going North!" )
        else:
            print("Can't move North\n")
    if direction == 's':
        if hasattr(c_room, 's_to'):
            c_room = c_room.s_to
            print("Going South!")
        else:
            print("Can't move South\n")

    if direction == 'i':
        print('\nChecking inventory...\n')
        if hasattr(p1, 'items'):
            for item in p1.items:
                print(
                    f'Item: {item.name}. {item.description}.\n')
        else:
            print("Inventory is empty\n")
# If the user enters "q", quit the game.
    if direction == 'q':
        print("Thanks for playing\nBye!\n")
        break

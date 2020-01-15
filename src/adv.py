from room import Room
from player import Player
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

player = Player('', room['outside'])

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

directions = {'n':'n_to', 'e':'e_to', 's':'s_to', 'w':'w_to'}

# Welcome the player to the game and take their Player name
def intro():
    player.name = input('What is your name Traveler?')
    print(f'\nWelcome to the game, {player.name}')

# Check if the user is going entering a new room, if they are we print the new room info
def location(player, prev_room = ''):
    if player.current_room.name != prev_room:
        print(f'\nCurrent Room: {player.current_room.name}')
        print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))

# Run the introduction and then print the player information to start the game
intro()
print(f'\nCurrent Room: {player.current_room.name}')
print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))

# Loop that allows player to enter movement and also is checking if they entered a new room or quit the game.
while True: 
    move = input('What direction would you like to go? \n(n, e ,s ,w)\n')
    if move in directions:
        prev_room = player.current_room.name
        player.current_room = player.current_room.enterRoom(directions[move])
        location(player, prev_room)
    elif move == 'q':
        print('\n Thanks for playing! \n')
        break
    else:
        print('\n You cannot go that way! \n')
from room import Room
from player import Player
from item import Item
import random
import textwrap

# slow typing
# import sys,time

# def print_slow(str):
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.1)

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

item = {
    'gauntlet':     Item('Gauntlet', 'Some glove with a lot of shiny rocks in it'),

    'lightsaber':   Item('Lightsaber', 'Flashlight weapon'),

    'slime':         Item('Slime', 'Slimey'),

    'bug':          Item('Bug', 'Chirp chirp'),

    'katana':       Item('Katana', 'A freakin Katana!'),

    'battery':      Item('Battery', 'Just a AA battery'),

    'spatula':      Item('Spatula', 'It is a spatula, pretty straight forward'),

    'coins':        Item('Coins', 'Money, money, money'),

    'sword':        Item('Sword', 'Looks sharp, be carful with that'),

    'mcnuggets':    Item('McNuggets', 'I am coding this while hungry')
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

# Add items to a room

room['outside'].item_list = [item[random.choice([*item.keys()])]]
room['foyer'].item_list = [item[random.choice([*item.keys()])], item[random.choice([*item.keys()])]]
room['overlook'].item_list = [item[random.choice([*item.keys()])], item[random.choice([*item.keys()])]]
room['narrow'].item_list = [item[random.choice([*item.keys()])]]
room['treasure'].item_list = [item[random.choice([*item.keys()])]]

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

directions = {'go north':'n_to', 'go east':'e_to', 'go south':'s_to', 'go west':'w_to'}

# Welcome the player to the game and take their Player name
def intro():
    player.name = input('What is your name Traveler?\n')
    print(f'\nWelcome to the game, {player.name}')

# Check if the user is going entering a new room, if they are we print the new room info
def location(player, prev_room = ''):
    if player.current_room.name != prev_room:
        print(f'\nCurrent Room: {player.current_room.name}')
        print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))
        print('In this room:')
        for i in player.current_room.item_list:
            print(f'{i.name}')

def inventory(player):
    print('\nInventory:')
    for i in player.inventory:
        print(f'\nItem Name: {i.name}\nDescription: {i.description}')

# Run the introduction and then print the player information to start the game
intro()
print(f'\nCurrent Room: {player.current_room.name}')
print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))
print('In this room:')
for i in player.current_room.item_list:
    print(f'{i.name}')

# Loop that allows player to enter movement and also is checking if they entered a new room or quit the game.
while True: 
    move = input('\nWhat would you like to do\n').lower()
    actions = move.split(' ')
    if move in directions:
        prev_room = player.current_room.name
        player.current_room = player.current_room.enterRoom(directions[move])
        location(player, prev_room)
    elif actions[0] == 'take':
            player.pickUp(player.inventory, item[actions[1]])
            print('Inventory: ')
            for i in player.inventory:
                print(f'{i.name}')
    elif actions[0] == 'drop':
            player.drop(player.inventory, item[actions[1]])
            print('Inventory: ')
            for i in player.inventory:
                print(f'{i.name}')
    elif actions[0] == 'inventory':
            inventory(player)
    elif move == 'quit':
        print('Thanks for playing! \n')
        break
    else:
        print('That is not a doable action \n')
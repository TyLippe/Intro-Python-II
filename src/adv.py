from room import Room
from player import Player
from item import Item
from monster import Monster
import random as r
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


# Declare all the items
item = {
    'gauntlet':     Item('Gauntlet', 'Some glove with a lot of shiny rocks in it'),
    'lightsaber':   Item('Lightsaber', 'Flashlight weapon'),
    'slime':        Item('Slime', 'Slimey'),
    'bug':          Item('Bug', 'Put that thing down'),
    'katana':       Item('Katana', 'A freakin Katana!'),
    'battery':      Item('Battery', 'Just a AA battery'),
    'spatula':      Item('Spatula', 'It is a spatula, pretty straight forward'),
    'coins':        Item('Coins', 'Money, money, money'),
    'sword':        Item('Sword', 'Looks sharp, be carful with that'),
    'mcnuggets':    Item('McNuggets', 'I am coding this while hungry'),
    'phone':        Item('Phone', 'Pretty sure it is cracked, totally not your fault'),
    'sweater':      Item('Sweater', 'Are you about to put this on? Gross...'),
    'sandwich':     Item('Sandwich', 'Still hungry'),
    'parrot':       Item('Parrot', 'Pretty sure you are a pirate now'),
}


# Adding some monster to the dugeon 
monster = {
    'dracula':  Monster('Dracula', 8),
    'godzilla': Monster('Godzilla', 12),
    'pikachu':  Monster('Pikachu', 4),
    'robot':    Monster('Robot', 8)
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


# Link items to a room, hardcoding sword to first room to prepare player for combat
room['outside'].item_list = [item['sword']]
room['foyer'].item_list = [item[r.choice([*item.keys()])], item[r.choice([*item.keys()])]]
room['overlook'].item_list = [item[r.choice([*item.keys()])], item[r.choice([*item.keys()])]]
room['narrow'].item_list = [item[r.choice([*item.keys()])]]
room['treasure'].item_list = [item[r.choice([*item.keys()])]]


# Link monsters to a room, no monster in first room
room['foyer'].monster_list = [monster['pikachu']]
room['overlook'].monster_list = [monster['dracula']]
room['narrow'].monster_list = [monster['robot']]
room['treasure'].monster_list = [monster['godzilla']]


# Make a new player object that is currently in the 'outside' room.
player = Player('', room['outside'], 0)


# Dictionary that holds directional input and the value tied to the input
directions = {'go north':'n_to', 'go east':'e_to', 'go south':'s_to', 'go west':'w_to'}


# Welcome's player to game and allows custom name input also shows player their hp
def intro():
    player.name = input('What is your name Traveler?\n')
    print(f'\nWelcome to the game, {player.name}')
    roll()
    print(f'You have {player.hp} health points! Be cautious!\n')


# Random num generator for health and attack points
def roll():
    player.hp = r.randint(1,10)


# Check if the user is going entering a new room, if they are print the new room info
def location(player, prev_room = ''):
    if player.current_room.name != prev_room:
        print(f'\nCurrent Room: {player.current_room.name}')
        print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))
        print('In this room:')
        for i in player.current_room.item_list:
            print(f'{i.name}')   
        print('\nMonster in this room:')
        for i in player.current_room.monster_list:
            print(f'{i.name}')     


# A quick view of a players inventory, prints name and description
def inventory(player):
    print('\nInventory:')
    for i in player.inventory:
        print(f'Item Name: {i.name}\nDescription: {i.description}\n')


# A view of all input options
def inputChoices():
    print('All Input`s Allowed:\n')
    print('Go North\nGo South\nGo East\nGo West\nTake `item`\nDrop `item`\nInventory\nHelp\nQuit')


# Introduce the player and let them know where they are currently
intro()
print(f'\nCurrent Room: {player.current_room.name}')
print(textwrap.fill(f'Description: {player.current_room.description}\n', 50))
print('In this room:')
for i in player.current_room.item_list:
    print(f'{i.name}')


# Loop that checks player actions and decides what to return
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
    elif move == 'inventory':
            inventory(player)
    elif move == 'help':
            inputChoices()
    elif move == 'quit':
        print('Thanks for playing! \n')
        break
    else:
        print('That is not a doable action \n')


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
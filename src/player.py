# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def pickUp(self, inventory, item):
        if item in self.current_room.item_list:
            print(f'You picked up {item.name}')
            inventory.append(item)
            self.current_room.item_list.remove(item)
        else:
            print('That item is not in here')


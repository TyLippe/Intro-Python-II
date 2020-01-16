class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    # Pick up item adds to player.inventory while removing from room.item_list
    def pickUp(self, inventory, item):
        if item in self.current_room.item_list:
            print(f'\nYou picked up {item.name}')
            inventory.append(item)
            self.current_room.item_list.remove(item)
        else:
            print('That item is not in here')
    # Drops item removes from player.inventory while adding to room.item_list
    def drop(self, inventory, item):
        if item in inventory:
            print(f'\nYou dropped {item.name}')
            inventory.remove(item)
            self.current_room.item_list.append(item)
        else:
            print('You cannot drop an item you do not have')


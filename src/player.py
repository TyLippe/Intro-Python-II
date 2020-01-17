class Player:
    def __init__(self, name, current_room, hp, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.hp = hp
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
    # Combat allows a player to fight a monster if monster has no health the monster should drop an item
    def combat(self, item, monster):
        if monster in self.current_room.monster_list:
            monster.hp -= item.attack
            print(f'You hit {monster.name} with {item.name} for {item.attack} damage!')
            print(f'{monster.name} has {monster.hp} hp left!')
            if monster.hp <= 0:
                self.current_room.item_list.append(monster.item)
                self.current_room.monster_list.remove(monster)
                print(f'You defeated {monster.name} and they dropped {monster.item.name}!')
        else:
            print('No reason to fight in here')
    # Equip will put the chosen item at the end of the list, making it default for fights
    def equip(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.inventory.append(item)
            print(f'You have equipped {item.name}')
        else:
            print('You do not have that item')

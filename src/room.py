# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description, item_list=[]):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
    # Function that will check if the room has the directions that the player inputs, if not they stay in their current room and are given a message
    def enterRoom(self, directions):
        new_room = self.__getattribute__(directions)
        if new_room == self:
            print('\nYou explore in that direction and find no where to go\n')
        return new_room

        

 
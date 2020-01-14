# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
    def enterRoom(self, directions):
        new_room = self.__getattribute__(directions)
        if new_room == self:
            print('\nYou explore in that direction and find no where to go\n')
        return new_room


 
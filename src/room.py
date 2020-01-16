class Room: 
    def __init__(self, name, description, item_list=[], monster_list=[]):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.monster_list = monster_list
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
    # Check if the current_room has the directions that the player inputs, if not player stays in current_room and print error
    def enterRoom(self, directions):
        new_room = self.__getattribute__(directions)
        if new_room == self:
            print('\nYou explore in that direction and find no where to go\n')
        return new_room

        

 
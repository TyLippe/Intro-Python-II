class Monster:
    def __init__(self, name, hp, attack, item=[]):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.item = item
    # Cannot let the user have all the fun
    def fightBack(self, player):
        if player.hp > 0:
            player.hp -= self.attack
            print(f'You were hit for {self.attack} damage!')
            print(f'You have {player.hp} hp left.')

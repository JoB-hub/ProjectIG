class Card:
    def __init__(self, name, ap, hp, cost):
        self.name = name
        self.ap = ap        # attack power
        self.hp = hp        # health points
        self.cost = cost    # cost of drawing a card
        self.already_attacked = False

    def __repr__(self):
        return '[' + self.name + ', ap:' + str(self.ap) + ', hp:' + str(self.hp) + ', cost:' + str(self.cost) + ']'

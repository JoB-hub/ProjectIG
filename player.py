from deck import decks
from board import sides
import random


class Player:
    def __init__(self, name, deck_no, side_no):
        self.deck = decks[deck_no][:]
        self.player_board = sides[side_no]
        random.shuffle(self.deck)
        self.name = name
        self.hand = []
        self.hp = 30
        self.mp = 0
        self.temp_mp = 0

    def add_to_hand(self):
        if len(self.deck) == 0:
            self.hp -= 1
        else:
            if len(self.hand) < 9:
                self.hand.append(self.deck.pop())
            else:
                self.deck.pop()

    def how_much_cards_in_hand(self):
        return len(self.hand)

    def __repr__(self):
        return f'''
Nickname: {self.name}
'''

class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.current_enemy = 1
        self.current_turn = False
        self.turn = 0
        self.game_over = 0

    def add_player(self, player):
        self.players.append(player)

    def delete_player(self, player):
        self.players.pop(player)

    def next_player(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    def deal_the_cards(self):
        for i in range(5):
            self.players[0].add_to_hand()
            self.players[1].add_to_hand()

    def choose_card(self, index):
        return self.players[self.current_player].hand.pop(index)

    def add_to_board(self, placement, card_index):
        if 6 > placement > 0 and self.players[self.current_player].player_board[placement - 1] == 0 and \
                self.players[self.current_player].hand[card_index-1].cost <= self.players[self.current_player].temp_mp:
            self.players[self.current_player].temp_mp -= self.players[self.current_player].hand[card_index-1].cost
            self.players[self.current_player].player_board[placement-1] = self.choose_card(card_index-1)
        else:
            print("No mana")

    def attack(self, index_attack):
        if self.players[self.current_player].player_board[index_attack-1] != 0:
            if self.players[self.current_enemy].player_board[index_attack-1] == 0:
                self.players[self.current_enemy].hp -= self.players[self.current_player].player_board[index_attack-1].ap
            else:
                self.players[self.current_enemy].player_board[index_attack-1].hp -= \
                    self.players[self.current_player].player_board[index_attack-1].ap
                if self.players[self.current_enemy].player_board[index_attack-1].hp <= 0:
                    self.players[self.current_enemy].player_board[index_attack-1] = 0

    def start_turn(self):
        if not self.current_turn:
            if self.players[self.current_player].hp <= 0:
                self.delete_player(self.current_player)
                self.next_player()
                self.current_turn = False
            else:
                self.players[self.current_player].add_to_hand()

                if self.current_player == 0:
                    self.current_enemy = 1
                else:
                    self.current_enemy = 0

                self.current_turn = True
                self.turn += 1

                if self.turn == 2:
                    self.players[self.current_player].mp += 2
                else:
                    if self.turn == 4:
                        pass
                    else:
                        if self.players[self.current_player].temp_mp < 10:
                            self.players[self.current_player].mp += 1

            self.players[self.current_player].temp_mp = self.players[self.current_player].mp

    def end_turn(self):
        if self.current_turn:
            self.current_turn = False
            if self.players[self.current_enemy].hp <= 0:
                self.delete_player(self.current_enemy)
            if len(self.players) == 1:
                print('GAME OVER')
            self.next_player()

    def __repr__(self):
        return f'''
        Turn: {self.turn}
{self.players[self.current_player].name} Hp: {self.players[self.current_player].hp} Mana: {self.players[self.current_player].temp_mp}
{self.players[self.current_player].hand}
    {self.players[self.current_player].player_board}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {self.players[self.current_enemy].player_board}
{self.players[self.current_enemy].hand}
{self.players[self.current_enemy].name} Hp: {self.players[self.current_enemy].hp} Mana: {self.players[self.current_enemy].temp_mp}
        '''

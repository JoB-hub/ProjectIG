from flask import Flask, render_template, request, redirect
from player import Player
from game import Game

app = Flask(__name__)

game = Game()


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/solo')
def solo():
    return render_template('solo.html')


@app.route('/solo_start', methods=['POST'])
def solo_start():
    global game
    game = Game()
    game.add_player(Player(request.form['Player 1'], 0, 0))
    game.add_player(Player(request.form['Player 2'], 1, 1))
    for i in range(5):
        game.players[0].add_to_hand()
        game.players[1].add_to_hand()
    game.start_turn()
    return redirect('/board')


@app.route('/board')
def board():
    global game
    return render_template('board.html', game=game)

# gra = Game()
#
# gracz = Player("Sam", 0, 0)
# gracz2 = Player("Bam", 1, 1)
#
# gra.add_player(gracz)
# gra.add_player(gracz2)
#
# gra.players[0].add_to_hand()
# gra.players[0].add_to_hand()
# gra.players[0].add_to_hand()
# gra.players[0].add_to_hand()
# gra.players[0].add_to_hand()
#
# gra.players[1].add_to_hand()
# gra.players[1].add_to_hand()
# gra.players[1].add_to_hand()
# gra.players[1].add_to_hand()
# gra.players[1].add_to_hand()
#
#
# gra.start_turn()
# gra.add_to_board(5, 6)
# print(gra.__repr__())
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print(gra.players[gra.current_player].player_board)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.end_turn()
#
# print("-----------------------")
#
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.end_turn()
#
# print("-----------------------")
#
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# gra.add_to_board(1, 5)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")
#
# gra.start_turn()
# print("Tura: " + str(gra.turn) + "      Gracz nr: " + str(gra.current_player) + "     HP: " + str(gra.players[gra.current_player].hp) + "     Stałe punkty many: " + str(gra.players[gra.current_player].mp) + "     Temp punkty many: " + str(gra.players[gra.current_player].temp_mp))
# print(gra.players[gra.current_player].hand)
# print("Plansza gracza: " + str(gra.players[gra.current_player].player_board))
# print("Plansza przeciwnika: " + str(gra.players[gra.current_enemy].player_board))
# gra.attack(1)
# gra.end_turn()
#
# print("-----------------------")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

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
    print(game.current_player)
    print(game.current_enemy)
    game.deal_the_cards()
    print(game.players[game.current_player].hand)
    print(game.players[game.current_enemy].hand)
    game.start_turn()
    return redirect('/board')


@app.route('/winner')
def winner():
    return render_template('winner.html')


@app.route('/board', methods=['POST', 'GET'])
def board():

    global game
    print(game.current_player)
    print(game.current_enemy)
    print(game.players[game.current_player].hand)
    print(game.players[game.current_enemy].hand)
    if len(game.players) > 1:
        if "choice" in request.form and "choice_board" in request.form and "end_turn" not in request.form:
            card_index = int(request.form["choice"])
            board_index = int(request.form["choice_board"])
            game.add_to_board(board_index, card_index)
        elif "end_turn" in request.form:
            if game.players[game.current_enemy].hp <=0:
                return redirect('/winner')
            game.end_turn()
            game.start_turn()
        elif "choice_board" in request.form  and "end_turn" not in request.form:
            card_index = int(request.form["choice_board"])
            game.attack(card_index)

    return render_template('board.html', game=game)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

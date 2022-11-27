from uuid import uuid4

from flask import Flask, render_template, request
from flask_socketio import (SocketIO, close_room, emit, join_room, leave_room,
                            send)

from game import (PlayRound, add_game, add_player, delete_game,
                  get_game_status, update_game)

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/newgame', methods=('GET', 'POST'))
def create():
    return '<p>This would return a form template to start a new game</p>'


@app.route('/<room>',  methods=('GET', 'POST'))
def play(room):
    """Players can join a room"""

    return '<p>This would render a template to play</p>'


@socketio.on('join')
def on_join(data):
    """
    Allows a user to join a room if allowed
    and adds their data to the room data
    """

    user_id = request.sid
    username = data['username']
    room = data['room']

    # You can't join a room if it doesn't exist
    game_status = get_game_status(room)
    if not game_status:
        emit(f'A game with id {room} does not exist')
        return
    # You can't join a room if it's full
    players = game_status.get('players', [])
    if len(players) > 1:
        print('This room is already full')
        return
    # Otherwise, join the room
    join_room(room)  # subscribe the socket that emitted the join event   
    send(username + ' has entered the room.', to=room)
    add_player(room, user_id, username)
    update_game(room, data)


@socketio.on('leave')
def on_leave(data):
    """If a leaves, the game ends"""

    username = data['username']
    room = data['room']
    leave_room(room)
    emit(f'{username} has ended the game. Good bye!', to=room)
    close_room(room)
    delete_game(room)


@socketio.on('create')
def on_create(data):
    """Creates a room by creating the data"""

    room = uuid4()
    add_game(room)

    return room


@socketio.on('play')
def on_play(data):
    """user makes a play and stuff happens"""

    user_id = data['user_id']
    room = data['room']
    move = data['move']

    round = PlayRound(room)
    round.handle_play(user_id, move)


if __name__ == '__main__':
    socketio.run(app)

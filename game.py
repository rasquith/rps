
from random import choice
from enum import Enum
from typing import Union


class RPSMove(Enum):
    """The game allows a finite set of moves"""

    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'


# no_sql database is not implemented, but could use something like MongoDB
# data looks like:
#     {
#         '<room_id>':
#             {
#                 'round': round the game is currently on,
#                 'completed_plays': when this is 2, move on,
#                 'computer_opponent': bool,
#                 'players': {
#                     some socket id: {
#                         'name': some usernamre
#                         'score': total score
#                         'round': can't be greater than overall round,
#                         'move': last move made
#                     },
#                     'computer or socket_id': {
#                         'name': some username,
#                         'score': total score
#                         'round': can't be greater than overall round,
#                         'move': last move made
#                     },
#                 }
#             }
#     }


def get_game_status(game_id: str) -> Union[dict, None]:
    """
    Queries data store to get a copy of the current game status.
    This function is fake and needs to be updated.
    Note: note implemented, but this can be used to determine whether
    the game should advance a round or whether a user can submit a guess.
    """

    # Returns a placeholder for now
    return {
                'round': 1,
                'completed_plays': 0,
                'computer_opponent': True,
                'players': {
                    'placeholder_sid': {
                        'name': 'user1',
                        'score': 1,
                        'round': 0,
                        'move': 'rock'
                    },
                    'computer': {
                        'name': 'computer',
                        'score': 1,
                        'round': 0,
                        'move': 'paper',
                    },
                }
            }


def add_game(game_id: str):
    """Add game to databse and initializes rounds, scores as 0"""

    return


def add_player(game_id: str, user_id: str, name: str):
    """Add player to game"""

    return


def update_game(game_id, data: dict):
    """Update game data"""

    return


def delete_game(game_id: str):
    """Remove a game froe a database"""
    return


def find_winner(first: RPSMove, second: RPSMove) -> bool:
    """Given two moves, find the winner"""

    winner_map = {
        RPSMove.ROCK: {RPSMove.PAPER: 2, RPSMove.SCISSORS: 1},
        RPSMove.PAPER: {RPSMove.SCISSORS: 2, RPSMove.ROCK: 1},
        RPSMove.SCISSORS: {RPSMove.ROCK: 2, RPSMove.PAPER: 1}
    }
    # This is a tie, nobody wins
    if first == second:
        return None
    return winner_map[first['move']][second['move']]


class PlayRound:
    """Manages one round of game play"""

    def __init__(self, game_id: str):
        self.game_id
        self.round_data = get_game_status(game_id)
        self.computer_opponent = self.round_data['computer_opponent']

    def handle_play(self, user_id, move):
        """
        Add a play.
        Optionally add a computer play.
        If the round is complete, find a winner and update the data store.
        """

        self._add_play(user_id, move)

        if self.computer_opponent:
            self._add_computer_play()
        # If both plays are completed, complete the round
        if self.round_data['completed_plays'] == 2:
            self._add_winner()
            self.update_round()

    def _add_winner(self):
        """
        Get the current choices.
        Find the winner.
        Update the score.
        """

        players = [k for k in self.round_data['players']]
        winner = find_winner(players[0]['move'], players[1]['move'])
        if winner is None:
            return
        # else update the score
        self.round_data[players[winner - 1]]['score'] += 1

    def update_round(self):
        """
        Update round in the current instance play data.
        Update the data in the data store (this is not cmplete).
        """

        self.round_data['round'] += 1
        update_game(self.game_id, self.round_data)

    def _add_play(self, user_id: str, move: RPSMove):
        """Update the current instance play data."""

        play = self.round_data['players'][user_id]
        play['round'] += 1
        play['move'] = move
        # TODO do we need this?
        self.round_data['player'][user_id].update(play)
        self.round_data['completed_plays'] += 1
        return

    def _add_computer_play(self):
        """Generate a move and update the current play data for computer"""

        move = choice(list(RPSMove))
        return self._add_play('computer', move)

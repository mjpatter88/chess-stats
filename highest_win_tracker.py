import chessdotcom
from typing import Optional

class UserInfo:
    def __init__(self, username, info) -> None:
        self.username = username
        self.best_rapid = _get_best_rating(info, 'chess_rapid')
        self.best_blitz = _get_best_rating(info, 'chess_blitz')
        self.best_bullet = _get_best_rating(info, 'chess_bullet')

class HighestWinTracker:
    def __init__(self) -> None:
        self.highest_rating = 0
        self.best_win_info = None
        self.best_opponent_info = None

    def add(self, game, username) -> None:
        white = game['white']
        black = game['black']
        if white['username'] == username:
            if white['result'] == 'win':
                self._process_game_opponent(game, black['username'])
        else:
            if black['result'] == 'win':
                self._process_game_opponent(game, white['username'])

    def _process_game_opponent(self, game, opponent):
        user_stats = chessdotcom.get_user_stats(opponent)
        best_rapid = _get_best_rating(user_stats, 'chess_rapid')
        best_blitz = _get_best_rating(user_stats, 'chess_blitz')
        best_bullet = _get_best_rating(user_stats, 'chess_bullet')

        user_info = UserInfo(opponent, user_stats)

        if best_rapid > self.highest_rating:
            self.highest_rating = best_rapid
            self.best_opponent_info = user_info
            self.best_win_info = game
        if best_blitz > self.highest_rating:
            self.highest_rating = best_blitz
            self.best_opponent_info = user_info
            self.best_win_info = game
        if best_bullet > self.highest_rating:
            self.highest_rating = best_bullet
            self.best_opponent_info = user_info
            self.best_win_info = game


    def best_win(self):
        return self.best_win_info

    def best_opponent(self) -> Optional[UserInfo]:
        return self.best_opponent_info


def _get_best_rating(user_stats, time_control):
    if time_control not in user_stats:
        return 0
    if 'best' not in user_stats[time_control]:
        return 0
    return user_stats[time_control]['best']['rating']



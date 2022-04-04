import requests
import chessdotcom
import highest_win_tracker

USERNAME='mjpatter88'

def run():
    user_profile = chessdotcom.get_user_profile(USERNAME)
    print(f"Username: {user_profile['username']}")

    user_stats = chessdotcom.get_user_stats(USERNAME)
    print(user_stats)
    print(f"Rapid: {user_stats['chess_rapid']['last']['rating']}")
    print(f"Blitz: {user_stats['chess_blitz']['last']['rating']}")
    print(f"Bullet: {user_stats['chess_bullet']['last']['rating']}")

    user_games = chessdotcom.get_user_games(USERNAME)
    print(f"Total games played: {len(user_games)}")

    tracker = highest_win_tracker.HighestWinTracker();
    # find all opponents that were beaten and find their highest rating in any time control.
    for index, game in enumerate(user_games):
        if(index % 50 == 0):
            print(f"{index},", end="", flush=True)
        tracker.add(game, USERNAME)

    print()
    opponent = tracker.best_opponent()
    best_game = tracker.best_win()

    if opponent:
        print("Opponent with highest rating in any time control:")
        print(opponent.username)
        print(f"Rapid: {opponent.best_rapid}")
        print(f"Blitz: {opponent.best_blitz}")
        print(f"Bullet: {opponent.best_bullet}")

    print("Game Info:")
    print(best_game)




if (__name__) == "__main__":
	run()

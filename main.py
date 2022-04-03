import requests
import chessdotcom

USERNAME='mjpatter88'

def run():
    user_profile = chessdotcom.get_user_profile(USERNAME)
    print(f"Username: {user_profile['username']}")

    user_stats = chessdotcom.get_user_stats(USERNAME)
    print(f"Rapid: {user_stats['chess_rapid']['last']['rating']}")
    print(f"Blitz: {user_stats['chess_blitz']['last']['rating']}")
    print(f"Bullet: {user_stats['chess_bullet']['last']['rating']}")

    user_games = chessdotcom.get_user_games(USERNAME)
    print(f"Total games played: {len(user_games)}")


if (__name__) == "__main__":
	run()

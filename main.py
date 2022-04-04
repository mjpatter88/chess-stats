import requests
import chessdotcom

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

    win_count = 0
    opponents = set()

    # find all opponents that were beaten and find their highest rating in any time control.
    for game in user_games:
        white = game['white']
        black = game['black']
        if white['username'] == USERNAME:
            if white['result'] == 'win':
                win_count += 1
                opponents.add(black['username'])
        else:
            if black['result'] == 'win':
                win_count += 1
                opponents.add(white['username'])

    print(f"Wins: {win_count}")
    print(f"Total unique opponents: {len(opponents)}")
    print(opponents.pop())

    highest_rating = 0
    highest_opp = ""
    highest_opp_type = ""

    for index, user in enumerate(opponents):
        if(index % 50 == 0):
            print(f"{index},", end="", flush=True)
        user_stats = chessdotcom.get_user_stats(user)
        best_rapid = _get_best_rating(user_stats, 'chess_rapid')
        best_blitz = _get_best_rating(user_stats, 'chess_blitz')
        best_bullet = _get_best_rating(user_stats, 'chess_bullet')

        if best_rapid > highest_rating:
            highest_rating = best_rapid
            highest_opp = user
            highest_opp_type = "rapid"
        if best_blitz > highest_rating:
            highest_rating = best_blitz
            highest_opp = user
            highest_opp_type = "blitz"
        if best_bullet > highest_rating:
            highest_rating = best_bullet
            highest_opp = user
            highest_opp_type = "bullet"

    print()
    print("Opponent with highest rating in any time control:")
    print(highest_opp)
    print(f"{highest_opp_type}: {highest_rating}")


def _get_best_rating(user_stats, time_control):
    if time_control not in user_stats:
        return 0
    if 'best' not in user_stats[time_control]:
        return 0
    return user_stats[time_control]['best']['rating']



if (__name__) == "__main__":
	run()

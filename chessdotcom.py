import requests

def get_user_profile(username):
    r = requests.get('https://api.chess.com/pub/player/{username}'.format(username=username))
    assert r.status_code == 200
    return r.json()

def get_user_stats(username):
    r = requests.get('https://api.chess.com/pub/player/{username}/stats'.format(username=username))
    assert r.status_code == 200
    return r.json()

def get_user_games(username):
    print("Downloading games...")
    games = []
    r = requests.get('https://api.chess.com/pub/player/{username}/games/archives'.format(username=username))
    assert r.status_code == 200

    archive = r.json()['archives']
    for month_archive_url in archive:
        games_response = requests.get(month_archive_url)
        print(".", end="", flush=True)
        games.extend(games_response.json()['games'])

    print("")
    return games

import requests

def fetch_player_stats():
    url = "https://cricapi.com/api/playerStats?apikey=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return data

player_stats = fetch_player_stats()
print(player_stats)

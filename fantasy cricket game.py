import random

class Player:
    def __init__(self, name, role, points_per_match):
        self.name = name
        self.role = role
        self.points_per_match = points_per_match

    def play_match(self):
        # Simulate match performance by generating random points
        return random.randint(0, self.points_per_match)

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_total_points(self):
        total_points = 0
        for player in self.players:
            total_points += player.play_match()
        return total_points

def create_players():
    # Example list of players
    players = [
        Player("Virat Kohli", "Batsman", 100),
        Player("Rohit Sharma", "Batsman", 90),
        Player("Jasprit Bumrah", "Bowler", 80),
        Player("MS Dhoni", "Wicketkeeper", 70),
        Player("Kieron Pollard", "Allrounder", 85)
    ]
    return players

def main():
    print("Welcome to Fantasy Cricket Game!")
    
    players = create_players()
    
    # Create a team
    team_name = input("Enter your team name: ")
    team = Team(team_name)
    
    print("Available players: ")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player.name} - {player.role}")
    
    # Team selection (let's say 5 players for simplicity)
    for _ in range(5):
        player_choice = int(input("Pick a player by number: "))
        selected_player = players[player_choice - 1]
        team.add_player(selected_player)
        print(f"{selected_player.name} added to your team.")
    
    print(f"\nTeam {team.name} has been created!\n")
    
    # Simulate match and calculate total points
    total_points = team.calculate_total_points()
    print(f"\nYour team earned {total_points} points in this match!")

if __name__ == "__main__":
    main()

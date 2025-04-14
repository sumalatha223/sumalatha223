class Player:
    def __init__(self, name, role, points_per_match, runs, wickets, catches):
        self.name = name
        self.role = role
        self.points_per_match = points_per_match
        self.runs = runs
        self.wickets = wickets
        self.catches = catches

    def calculate_points(self):
        # Calculate points based on runs, wickets, and catches
        points = self.runs * 0.1 + self.wickets * 10 + self.catches * 5
        return points

    def play_match(self):
        return self.calculate_points()

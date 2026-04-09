# agent.py — Agent/Robot that follows the planned path

class Agent:
    def __init__(self, start):
        self.position = start       # current (row, col)
        self.path = []              # list of waypoints
        self.path_index = 0         # which waypoint we're at
        self.steps_taken = 0
        self.reached_goal = False

    def set_path(self, path):
        """Assign a computed path to the agent."""
        self.path = path
        self.path_index = 0

    def move(self):
        """Move one step forward along the path."""
        if self.path_index + 1 < len(self.path):
            self.path_index += 1
            self.position = self.path[self.path_index]
            self.steps_taken += 1
        else:
            self.reached_goal = True

    def is_done(self):
        return self.reached_goal
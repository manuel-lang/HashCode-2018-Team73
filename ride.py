class Ride:
    def __init__(self, start_position, target_position, distance, earliest_start, latest_finish):
        self.s_position = start_position
        self.t_position = target_position
        self.distance = distance
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

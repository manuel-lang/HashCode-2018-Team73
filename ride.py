class Ride:
    def __init__(self, index, start_position, target_position, earliest_start, latest_finish):
        self.index = index
        self.valid = True
        self.s_position = start_position
        self.t_position = target_position
        self.distance = abs(target_position[1] - start_position[1]) + abs(target_position[0] - start_position[0])
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

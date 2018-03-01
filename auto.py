class Auto:
    def __init__(self, index, position=(0,0), is_driving = False, t_free = 0, rides_started = []):
        self.position = position
        self.is_driving = is_driving
        self.index = index
        self.t_free = t_free
        self.rides_started = rides_started

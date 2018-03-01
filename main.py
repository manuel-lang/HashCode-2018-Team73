import Ride

num_rows = 0;
num_cols = 0;
num_vehicles = 0;
num_rides = 0;
bonus = 0;
timesteps = 0;

def read_input():
    with open('a_example.in', 'r') as file:
        content = file.readlines()
        line1 = True
        rides = []
        for idx, line in enumerate(content):
            values = line.split(' ')
            if idx == 0:
                num_rows = values[0]
                num_cols = values[1]
                num_vehicles = values[2]
                num_rides = values[3]
                bonus = values[4]
                timesteps = values[5]
            else:
                rides.append(Ride())
                print(line)

                print(values)


read_input()


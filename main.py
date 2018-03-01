import auto
from ride import Ride

num_rows = 0;
num_cols = 0;
num_vehicles = 0;
num_rides = 0;
bonus = 0;
timesteps = 0;

def read_input():
    with open('data/a_example.in', 'r') as file:
        content = file.readlines()
        rides = []
        for idx, line in enumerate(content):
            line.rstrip()

            values = line.split(' ')
            if idx == 0:
                num_rows = int(values[0])
                num_cols = int(values[1])
                num_vehicles = int(values[2])
                num_rides = int(values[3])
                bonus = int(values[4])
                timesteps = int(values[5])
            else:
                rides.append(Ride((int(values[0]), int(values[1])), (int(values[2]), int(values[3])), int(values[4]), int(values[5])))
        return rides

def main():
    rides = read_input()

if __name__ == "__main__":
    main()

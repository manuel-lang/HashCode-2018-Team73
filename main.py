from auto import Auto
from ride import Ride

num_rows = 0
num_cols = 0
num_vehicles = 0
num_rides = 0
bonus = 0
timesteps = 0

def read_input():
    with open('data/a_example.in', 'r') as file:
        content = file.readlines()
        rides = []
        for idx, line in enumerate(content):
            line.rstrip()

            values = line.split(' ')
            if idx == 0:
                global num_rows
                global num_cols
                global num_vehicles
                global num_rides
                global bonus
                global timesteps

                num_rows = int(values[0])
                num_cols = int(values[1])
                num_vehicles = int(values[2])
                num_rides = int(values[3])
                bonus = int(values[4])
                timesteps = int(values[5])
            else:
                rides.append(Ride(idx, (int(values[0]), int(values[1])), (int(values[2]), int(values[3])), int(values[4]), int(values[5])))
        return rides

def write_output(vehicles):
    with open('output.txt', 'w') as file:
        for vehicle in vehicles:
            line = str(len(vehicle.rides_started))
            for ride_index in range(len(vehicle.rides_started)):
                line += " " + str(vehicle.rides_started[ride_index])
            line += "\n"
            file.write(line)
    file.close()

rides = read_input()
vehicles = []

def main():
    generateVehicles()
    for t in range(timesteps):
        removeImpossible(t)
        for vehicle in vehicles:
            if (vehicle.t_free <= t):
                ride_index = pickRide(vehicle.position, t)
                if ride_index != -1:
                    vehicle.rides_started.append(ride_index)
                    vehicle.t_free = t + calcDistance(vehicle.position,rides[ride_index].s_position) + max(0, rides[ride_index].earliest_start - (t + calcDistance(vehicle.position,rides[ride_index].s_position))) + rides[ride_index].distance
                    rides[ride_index].valid = False
                    vehicle.position = rides[ride_index].t_position
    write_output(vehicles)

def generateVehicles():
    for i in range(num_vehicles):
        vehicles.append(Auto(index = i))

def removeImpossible(t):
    for i in range(len(rides)):
        if(rides[i].latest_finish-rides[i].distance < t):
            rides[i].valid = False

def calcDistance(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def pickRide(pos,t): # Position vom Auto

    min_d = 99999999999
    min_index = -1

    for i in range(len(rides)):
        d = rides[i].latest_finish-rides[i].distance-calcDistance(pos,rides[i].s_position)

        if d < min_d and rides[i].valid:
            min_d = d
            min_index = i

    return min_index

if __name__ == "__main__":
    main()

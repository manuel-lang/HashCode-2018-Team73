from ride import Ride
from sys import argv
from vehicle import Vehicle

def write_output(vehicles):
    with open('output.txt', 'w') as file:
        for vehicle in vehicles:
            file.write(str(len(vehicle.rides_started)) + " " + " ".join(str(x) for x in vehicle.rides_started) + "\n")

def generateVehicles(numvehicles):
    vehicles = []
    for i in range(numvehicles):
        vehicles.append(Vehicle(i))
    return vehicles

def removeImpossible(rides, t):
    for i in range(len(rides)):
        if(rides[i].latest_finish-rides[i].distance < t):
            rides[i].valid = False

def calcDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def pickRide(rides, pos, t): # Vehicle position
    min_d = 99999999999
    min_index = -1
    for i in range(len(rides)):
        d = calcDistance(pos,rides[i].s_position) + max(0, rides[i].earliest_start - (t + calcDistance(pos,rides[i].s_position))) + rides[i].distance
        if d < min_d and rides[i].valid:
            min_d = d
            min_index = i

    return min_index

def main():
    filename = argv[1]
    numvehicles = 0
    timesteps = 0
    rides = []
    with open(filename, 'r') as file:
        content = file.readlines()
        for idx, line in enumerate(content):
            values = [int(x) for x in line.rstrip().split(" ")]
            if idx == 0:
                numvehicles = values[2]
                timesteps = values[5]
            else:
                rides.append(Ride(idx, (values[0], values[1]), (values[2], values[3]), values[4], values[5]))
    vehicles = generateVehicles(numvehicles)
    for t in range(timesteps):
        removeImpossible(rides, t)
        for vehicle in vehicles:
            if (vehicle.t_free <= t):
                ride_index = pickRide(rides, vehicle.position, t)
                if ride_index != -1:
                    vehicle.rides_started.append(ride_index)
                    vehicle.t_free = t + calcDistance(vehicle.position,rides[ride_index].s_position) + max(0, rides[ride_index].earliest_start - (t + calcDistance(vehicle.position,rides[ride_index].s_position))) + rides[ride_index].distance
                    rides[ride_index].valid = False
    write_output(vehicles)

if __name__ == "__main__":
    main()

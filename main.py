from auto import Auto
from ride import Ride
from sys import argv

def write_output(vehicles):
    with open('output.txt', 'w') as file:
        for vehicle in vehicles:
            line = str(len(vehicle.rides_started))
            for ride_index in range(len(vehicle.rides_started)):
                line += " " + str(vehicle.rides_started[ride_index])
            file.write(line + "\n")

def generateVehicles(numvehicles):
    vehicles = []
    for i in range(numvehicles):
        vehicles.append(Auto(i))
    return vehicles

def removeImpossible(rides, t):
    for i in range(len(rides)):
        if(rides[i].latest_finish-rides[i].distance < t):
            rides[i].valid = False

def calcDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def pickRide(rides, pos, t): # Position vom Auto
    min_d = 99999999999
    min_index = -1
    for i in range(len(rides)):
        d = calcDistance(pos,rides[i].s_position) + max(0, rides[i].earliest_start - (t + calcDistance(pos,rides[i].s_position))) + rides[i].distance#rides[i].latest_finish-rides[i].distance-calcDistance(pos,rides[i].s_position)
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
            line.rstrip()
            values = line.split(' ')
            if idx == 0:
                numvehicles = int(values[2])
                timesteps = int(values[5])
            else:
                rides.append(Ride(idx, (int(values[0]), int(values[1])), (int(values[2]), int(values[3])), int(values[4]), int(values[5])))

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

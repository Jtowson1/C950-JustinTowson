import csv
import datetime

from HashTable import HashTable

if __name__ == '__main__':
    hashtable = HashTable()
    First_truck = [1, 4, 13, 14, 15, 16, 19, 20, 21, 26, 29, 30, 34, 37, 40]
    Second_truck = [2, 3, 6, 18, 25, 28, 31, 32, 36, 38]
    Third_truck = [5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39]
    All_trucks = [First_truck, Second_truck, Third_truck]
    First_time = '8:00:00'
    Second_time = '9:10:00'
    Third_time = '11:00:00'
    First_truck_sorted = []
    Second_truck_sorted = []
    Third_truck_sorted = []
    total_distance = []

    with open('WGUPS_Package_File.csv', 'r') as csvfile:
        packageData = csv.reader(csvfile, delimiter=',')
        for row in packageData:
            packageID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            special = row[7]
            deliver_start = ''
            deliver_status = 'At Hub'
            delivery_time = ''
            package = (
                packageID, address, city, state, zipcode, deadline, weight, special, deliver_start, deliver_status,
                delivery_time)
            hashtable.insert(packageID, package)

    distanceNameData = []
    with open('Distance_Name_Data.csv') as csvfile:
        address_list = list(csv.reader(csvfile, delimiter=','))
        for data in address_list:
            distanceNameData.append(data[2])

    with open('Distance_Data.csv') as csvfile:
        distanceData = list(csv.reader(csvfile, delimiter=','))


        def getDistance(_row, _column):
            distance = distanceData[_row][_column]
            if distance == '':
                distance = distanceData[_column][_row]

            return float(distance)


    def set_deliver_start_time():
        for j in range(len(All_trucks)):
            if j == 1:
                for i in First_truck:
                    start_time = list(hashtable.search(i))
                    start_time[8] = First_time
                    hashtable.insert(i, tuple(start_time))
            elif j == 2:
                for i in Second_truck:
                    start_time = list(hashtable.search(i))
                    start_time[8] = Second_time
                    hashtable.insert(i, tuple(start_time))
            else:
                for i in Third_truck:
                    start_time = list(hashtable.search(i))
                    start_time[8] = Third_time
                    hashtable.insert(i, tuple(start_time))


    def first_truck_best_route():
        current_location = 0
        first_total_distance = 0
        while len(First_truck) > 0:
            next_location = distanceNameData.index(hashtable.search(First_truck[0])[1])
            new_location = next_location
            packageIndex = First_truck[0]
            shortest_distance = getDistance(current_location, next_location)
            for i in First_truck:
                next_location = distanceNameData.index(hashtable.search(i)[1])
                getDistance(current_location, next_location)
                if len(First_truck) == 1:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
                elif getDistance(current_location, next_location) < shortest_distance:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
            First_truck_sorted.append(packageIndex)
            First_truck.pop(First_truck.index(packageIndex))
            current_location = new_location
            first_total_distance += shortest_distance
        total_distance.append(first_total_distance)


    def second_truck_best_route():
        current_location = 0
        second_total_distance = 0
        while len(Second_truck) > 0:
            next_location = distanceNameData.index(hashtable.search(Second_truck[0])[1])
            new_location = next_location
            packageIndex = Second_truck[0]
            shortest_distance = getDistance(current_location, next_location)
            for i in Second_truck:
                next_location = distanceNameData.index(hashtable.search(i)[1])
                getDistance(current_location, next_location)
                if len(Second_truck) == 1:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
                elif getDistance(current_location, next_location) < shortest_distance:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
            Second_truck_sorted.append(packageIndex)
            Second_truck.pop(Second_truck.index(packageIndex))
            current_location = new_location
            second_total_distance += shortest_distance
        total_distance.append(second_total_distance)


    def third_truck_best_route():
        current_location = 0
        third_total_distance = 0
        while len(Third_truck) > 0:
            next_location = distanceNameData.index(hashtable.search(Third_truck[0])[1])
            new_location = next_location
            packageIndex = Third_truck[0]
            shortest_distance = getDistance(current_location, next_location)
            for i in Third_truck:
                next_location = distanceNameData.index(hashtable.search(i)[1])
                getDistance(current_location, next_location)
                if len(Third_truck) == 1:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
                elif getDistance(current_location, next_location) < shortest_distance:
                    shortest_distance = getDistance(current_location, next_location)
                    new_location = next_location
                    packageIndex = i
            Third_truck_sorted.append(packageIndex)
            Third_truck.pop(Third_truck.index(packageIndex))
            current_location = new_location
            third_total_distance += shortest_distance
        total_distance.append(third_total_distance)


    set_deliver_start_time()
    first_truck_best_route()
    second_truck_best_route()
    third_truck_best_route()
    All_trucks_sorted = [First_truck_sorted, Second_truck_sorted, Third_truck_sorted]


    def set_delivery_time():
        for i in range(len(All_trucks_sorted)):
            if i == 0:
                first_time = '8:00:00'
                (h, m, s) = first_time.split(':')
                First_time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                deliver_time = getDistance(0, distanceNameData.index(
                    hashtable.search(First_truck_sorted[0])[1])) / 18 * 60 * 60
                deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                First_time_object = First_time_object + deliver_time_seconds
                delivered_time = list(hashtable.search(First_truck_sorted[0]))
                delivered_time[10] = str(First_time_object)
                hashtable.insert(First_truck_sorted[0], tuple(delivered_time))
                for j in range(len(First_truck_sorted) - 1):
                    deliver_time = getDistance(distanceNameData.index(hashtable.search(First_truck_sorted[j])[1]),
                                               distanceNameData.index(
                                                   hashtable.search(First_truck_sorted[j + 1])[1])) / 18 * 60 * 60
                    deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                    First_time_object = First_time_object + deliver_time_seconds
                    delivered_time = list(hashtable.search(First_truck_sorted[j + 1]))
                    delivered_time[10] = str(First_time_object)
                    hashtable.insert(First_truck_sorted[j + 1], tuple(delivered_time))
            elif i == 1:
                second_time = '9:10:00'
                (h, m, s) = second_time.split(':')
                Second_time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                deliver_time = getDistance(0, distanceNameData.index(hashtable.search(Second_truck_sorted[0])[1])) / 18 * 60 * 60
                deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                Second_time_object = Second_time_object + deliver_time_seconds
                delivered_time = list(hashtable.search(Second_truck_sorted[0]))
                delivered_time[10] = str(Second_time_object)
                hashtable.insert(Second_truck_sorted[0], tuple(delivered_time))
                for j in range(len(Second_truck_sorted) - 1):
                    deliver_time = getDistance(distanceNameData.index(hashtable.search(Second_truck_sorted[j])[1]), distanceNameData.index(hashtable.search(Second_truck_sorted[j + 1])[1])) / 18 * 60 * 60
                    deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                    Second_time_object = Second_time_object + deliver_time_seconds
                    delivered_time = list(hashtable.search(Second_truck_sorted[j + 1]))
                    delivered_time[10] = str(Second_time_object)
                    hashtable.insert(Second_truck_sorted[j + 1], tuple(delivered_time))
            else:
                third_time = '11:00:00'
                (h, m, s) = third_time.split(':')
                Third_time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                deliver_time = getDistance(0, distanceNameData.index(hashtable.search(Third_truck_sorted[0])[1])) / 18 * 60 * 60
                deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                Third_time_object = Third_time_object + deliver_time_seconds
                delivered_time = list(hashtable.search(Third_truck_sorted[0]))
                delivered_time[10] = str(Third_time_object)
                hashtable.insert(Third_truck_sorted[0], tuple(delivered_time))
                for j in range(len(Third_truck_sorted) - 1):
                    deliver_time = getDistance(distanceNameData.index(hashtable.search(Third_truck_sorted[j])[1]), distanceNameData.index(hashtable.search(Third_truck_sorted[j + 1])[1])) / 18 * 60 * 60
                    deliver_time_seconds = datetime.timedelta(seconds=deliver_time)
                    Third_time_object = Third_time_object + deliver_time_seconds
                    delivered_time = list(hashtable.search(Third_truck_sorted[j + 1]))
                    delivered_time[10] = str(Third_time_object)
                    hashtable.insert(Third_truck_sorted[j + 1], tuple(delivered_time))

    set_delivery_time()

    print("Hello and Welcome to WGUPS User Interface!")
    print("Menu Options:")
    print("0 - Look up the status and information of a single package by the id and time")
    print("1 - Look up the status and information of all packages at a certain time")
    print("2 - Check the total mileage driven by the trucks")
    choice = int(input("Please enter your option: "))
    if choice == 0:
        id_choice = int(input("Please enter the package id you would like to search (1-40) "))
        time_choice = input("Please enter the time you would like to check (HH:MM:SS): ")
        (H, M, S) = time_choice.split(':')
        user_time_object = datetime.timedelta(hours=int(H), minutes=int(M), seconds=int(S))
        (h, m, s) = hashtable.search(id_choice)[10].split(':')
        delivered_time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (hh, mm, ss) = hashtable.search(id_choice)[8].split(':')
        start_time_object = datetime.timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))
        if user_time_object < start_time_object:
            print("ID: " + str(hashtable.search(id_choice)[0]) + " Address: " + hashtable.search(id_choice)[1] + " City: " + hashtable.search(id_choice)[2] +
                  " Zipcode: " + hashtable.search(id_choice)[4] + " Deadline: " + hashtable.search(id_choice)[5] + " Package Weight: " + hashtable.search(id_choice)[6] +
                  " Status: " + hashtable.search(id_choice)[9] + " Leaves hub at: " + hashtable.search(id_choice)[8])
        elif start_time_object < user_time_object < delivered_time_object:
            status = list(hashtable.search(id_choice))
            status[9] = "En route"
            hashtable.insert(id_choice, tuple(status))
            print("ID: " + str(hashtable.search(id_choice)[0]) + " Address: " + hashtable.search(id_choice)[1] + " City: " + hashtable.search(id_choice)[2] +
                  " Zipcode: " + hashtable.search(id_choice)[4] + " Deadline: " + hashtable.search(id_choice)[5] + " Package Weight: " + hashtable.search(id_choice)[6] +
                  " Status: " + hashtable.search(id_choice)[9] + " Left hub at: " + hashtable.search(id_choice)[8])
        elif user_time_object > delivered_time_object:
            status = list(hashtable.search(id_choice))
            status[9] = "Delivered"
            hashtable.insert(id_choice, tuple(status))
            print("ID: " + str(hashtable.search(id_choice)[0]) + " Address: " + hashtable.search(id_choice)[1] + " City: " + hashtable.search(id_choice)[2] +
                  " Zipcode: " + hashtable.search(id_choice)[4] + " Deadline: " + hashtable.search(id_choice)[5] + " Package Weight: " + hashtable.search(id_choice)[6] +
                  " Status: " + hashtable.search(id_choice)[9] + " Left hub at: " + hashtable.search(id_choice)[8] + " Delivered at: " + hashtable.search(id_choice)[10])
    elif choice == 1:
        time_choice1 = input("Please enter a time for status of all packages (HH:MM:SS): ")
        for i in range(1, 41):
            (h, m, s) = time_choice1.split(':')
            user_time_choice1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (H, M, S) = hashtable.search(i)[10].split(':')
            delivered_time_object = datetime.timedelta(hours=int(H), minutes=int(M), seconds=int(S))
            (hh, mm, ss) = hashtable.search(i)[8].split(':')
            start_time_object = datetime.timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))
            if user_time_choice1 < start_time_object:
                print("ID: " + str(hashtable.search(i)[0]) + " Address: " + hashtable.search(i)[1] + " City: " + hashtable.search(i)[2] +
                      " Zipcode: " + hashtable.search(i)[4] + " Deadline: " + hashtable.search(i)[5] + " Package Weight: " + hashtable.search(i)[6] +
                      " Status: " + hashtable.search(i)[9] + " Leaves hub at: " + hashtable.search(i)[8])
            elif start_time_object < user_time_choice1 < delivered_time_object:
                status = list(hashtable.search(i))
                status[9] = "En route"
                hashtable.insert(i, tuple(status))
                print("ID: " + str(hashtable.search(i)[0]) + " Address: " + hashtable.search(i)[1] + " City: " + hashtable.search(i)[2] +
                      " Zipcode: " + hashtable.search(i)[4] + " Deadline: " + hashtable.search(i)[5] + " Package Weight: " + hashtable.search(i)[6] +
                      " Status: " + hashtable.search(i)[9] + " Left hub at: " + hashtable.search(i)[8])
            elif user_time_choice1 > delivered_time_object:
                status = list(hashtable.search(i))
                status[9] = "Delivered"
                hashtable.insert(i, tuple(status))
                print("ID: " + str(hashtable.search(i)[0]) + " Address: " + hashtable.search(i)[1] + " City: " + hashtable.search(i)[2] +
                      " Zipcode: " + hashtable.search(i)[4] + " Deadline: " + hashtable.search(i)[5] + " Package Weight: " + hashtable.search(i)[6] +
                      " Status: " + hashtable.search(i)[9] + " Left hub at: " + hashtable.search(i)[8] + " Delivered at: " + hashtable.search(i)[10])
            else:
                print("Invalid entry please try again.")
    elif choice == 2:
        print("Total miles driven by truck 1 is: " + str(total_distance[0]))
        print("Total miles driven by truck 2 is: " + str(total_distance[1]))
        print("Total miles driven by truck 3 is: " + str(total_distance[2]))
        print("Total miles driven by all trucks is: " + str(round(sum(total_distance), 2)))
    else:
        print("Not a valid choice, please try again")

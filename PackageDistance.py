
import datetime
import CSV
import Hash_Table

# ---------------------------------------------------------------------------------------------------------------------
# list of package hash table
package_hash = Hash_Table.Hash_Table()

# my list for the distances between addresses
address_graph = []

# returns total number of destination in the file and adds them to the address_graph
totalNumVertex = CSV.loadPackageDistanceData('WGUPS Distance Table.csv', address_graph)

# return the total number of packages in the file and saves them in to the package hash table as a packageDis object
totalPacks = CSV.loadPackageDataWithDistance('PackageFile.csv', package_hash, address_graph)


# this method will return the distance between two packages using their ids
# in order for this method to work, the packages need to have distance ID
# the distance id is the vertex where the package will be delivered

def getDistance_id(pointA, pointB):
    myList = address_graph

    # this if statement is design specificlly for the hub since its not a package but
    # still needs to mesure the distance
    if pointA == 0:
        Address1_id = 1
    if pointA != 0:
        pointA = package_hash.search_package(pointA)
        Address1_id = int(pointA.distanceID)

    addressIndex = Address1_id - 1
    pointB = package_hash.search_package(pointB)

    Address2_id = int(pointB.distanceID)
    Distance = myList[Address2_id][addressIndex + 3]

    if Distance == "":
        # print("empty")
        addressIndex = Address2_id - 1
        Distance = myList[Address1_id][addressIndex + 3]

    # print("Distance: ", Distance)
    # Convert Distance from string to int
    Distance = float(Distance)
    return Distance


# .3 miles per minute 18 per hour
def playting_with_time2( s_time , distance_a):
    # this will get the minutes
    result = float(distance_a) / .3
    # this will get the seconds
    deci = result % 1
    result = round(result,0)
    d_minutes = result
    d_seconds = round(deci * 60,0)

    # s_time = datetime.timedelta(hours=8, minutes = 0)
    space_time2 = datetime.timedelta(seconds=d_seconds, minutes=d_minutes)
    # print(space_time2)
    total_time = space_time2 + s_time
    end_time = total_time
    # print("Final Time ", end_time)
    # the method will return the time
    return end_time


# this method will use the official route created by the NearestN method
# this method will load the trucks with the packages and send them to their location
# the method will take the truck number and the route list with the vertex
def Truck_on_Road(list_a,truck_number):
    stop_time = datetime.timedelta(hours=9, minutes=0)
    route_list = list_a
    print(route_list[0][4])

    # this method will load the package to the right truck
    for i in route_list[0][4]:

        k = package_hash.search_package(i)
        if truck_number == 1:
         k.deliveryStatus = "en route in truck one "
        else:
         k.deliveryStatus = "en route in truck two "




    starting_point = 0
    dis = 0
    start_time = route_list[0][1]
    time_a = start_time
    #stop_time = chosen_time

    # this loop will mark the time and distance of the packages
    for i in range(len(route_list[0][4])):

        b = route_list[0][4][i]
        a = starting_point

        # this statement will get the distance from one package to the other
        distance = getDistance_id(a, b)
        # using the distance, this method will calculate the time
        time_a = playting_with_time2(time_a, distance)
        #print("id ", b, " distance", distance, "time", time_a)



        # the delivery status is changed here
        j = package_hash.search_package(b)


        if truck_number == 1:
           j.deliveryStatus = "Truck one delivered packages at : {}".format(time_a)
        else:
           j.deliveryStatus = "Truck two delivered packages at : {}".format(time_a)

        '''route_list[0][3].pop(i)
        route_list[0][3].insert(i,0)'''

        if j.ID == 9:

            a_time = datetime.timedelta(hours=10, minutes=20)
            if time_a < a_time:
                j.deliveryStatus = "Not Delivered"

        dis = dis + distance
        starting_point = route_list[0][4][i]

        ''' a_time = datetime.timedelta(hours=10, minutes=15)
        b_time = datetime.timedelta(hours=10, minutes=30)
        
        if 
        if ((time_a > a_time) & (time_a < b_time)):
                 print("time for 9")


                 if (route_list[0][4].count(9) < 1):
                     print("package id 9 had wrong address. It is added to the list again. ")
                     h = package_hash.search(9)
                     h.distanceID = '20'
                     print()
                     route_list[0][4].append(9)
                     #route_list[0][4][1].append('20')
                     #unvisited_list = chosen_packList[0][3][0]'''


    hub_distance = getDistance_id(0, b)
    arrival_time = playting_with_time2(time_a, hub_distance)




    print("Starting from the Hub at: {}".format(start_time))
    for i in route_list[0][4]:
         print("\n", package_hash.search_package(i))



    print("\nHub    Distance: %s   Time: %s \n" % ( hub_distance, arrival_time))

    print("Total Distance", dis + hub_distance)
    print("Total Packages:", len(route_list[0][4]))
    print("visited list ", route_list[0][4], "\n\n")
    route_list[0][1] = arrival_time

    return dis +hub_distance



# This method is for checking the status of the package at a certain time
# this method will get the route list, truck number and stop time
#  the rest is the same as the method above
def Truck_on_Road_custTime(list_a,truck_number,stop_Time):
    stop_time = datetime.timedelta(hours=9, minutes=0)
    route_list = list_a
    print(route_list[0][4])


    for i in route_list[0][4]:

        k = package_hash.search_package(i)
        if truck_number == 1:
         k.deliveryStatus = "en route in truck one "
        else:
         k.deliveryStatus = "en route in truck two "




    starting_point = 0
    dis = 0
    start_time = route_list[0][1]
    time_a = start_time
    #stop_time = chosen_time

    for i in range(len(route_list[0][4])):

        b = route_list[0][4][i]
        a = starting_point

        distance = getDistance_id(a, b)
        time_a = playting_with_time2(time_a, distance)
        #print("id ", b, " distance", distance, "time", time_a)
        # the location and stop time if key for this method to work
        if (time_a > stop_Time):
              break

        j = package_hash.search_package(b)
        if truck_number == 1:
           j.deliveryStatus = "Truck one delivered packages at : {}".format(time_a)
        else:
           j.deliveryStatus = "Truck two delivered packages at : {}".format(time_a)
        '''route_list[0][3].pop(i)
        route_list[0][3].insert(i,0)'''


        dis = dis + distance
        starting_point = route_list[0][4][i]

        if j.ID == 9:

            a_time = datetime.timedelta(hours=10, minutes=20)
            if time_a < a_time:
                j.deliveryStatus = "Not Delivered"

        '''a_time = datetime.timedelta(hours=10, minutes=15)
        b_time = datetime.timedelta(hours=10, minutes=30)'''




    hub_distance = getDistance_id(0, b)
    arrival_time = playting_with_time2(time_a, hub_distance)



'''
    print("Starting from the Hub at: {}".format(start_time))
    for i in route_list[0][4]:
         print("\n", package_hash.search(i))



    print("\nHub    Distance: %s   Time: %s \n" % ( hub_distance, arrival_time))

    print("Total Distance", dis + hub_distance)
    print("Total Packages:", len(route_list[0][4]))
    print("visited list ", route_list[0][4], "\n\n")'''





'''

def get_package(point_a, my_list):
    distance_id = point_a

    for i in range(1, 40):
        h = my_list.search(i)

        if distance_id == int(h.distanceID):
            print("Package Id: %s       Address: %s        Vertex: %s " % (h.ID, h.address, h.distanceID))
'''

# The max is 26 or it will be out of range
# the min is is 0

'''
def getDistance(pointA, pointB, myList):
    Address1_id = int(pointA)
    Address2_id = int(pointB)
    addressIndex = Address1_id - 1
    print(Address2_id, addressIndex + 3)
    Distance = myList[Address2_id][addressIndex + 3]

    # print("\n\nAddress1: ", myList[0][addressIndex])
    # print("Address2: ", myList[Address2_id][1])

    if Distance == "":
        # print("empty")
        addressIndex = Address2_id - 1
        Distance = myList[Address1_id][addressIndex + 3]

    # print("Distance: ", Distance)
    # Convert Distance from string to int
    Distance = float(Distance)
'''



import datetime
import PackageDistance
import GreedyAlgo

# ---------------------------------------------------------------------------------------------------------------------


# This method will will return the route using the nearest neighbor principals
#Some variables might seem redundant but I left them there in case I needed them later for this project

def NearestN(start_packList, id_time_packCount,chosen_packList):
    pack_list =PackageDistance.package_hash
    visi_list =id_time_packCount[0][3]# this list is returned to use it again not add the vertex that were visited
    route_list = id_time_packCount[0][4]# this list has the official route for the truck to follow later

    #this variable in the list will change during this method and add all the packages mainly for the inner recursion
    pack_count = id_time_packCount[0][2]
    startVertex = id_time_packCount[0][0]#used for the recursion so it know where to start from
    arrival_time = id_time_packCount[0][1]# this time variable changes during the method and gives the time
    unvisited_list = start_packList# this list gives the starting vertex such as the ten thrity list from the greedyAlgo
    weight_list = []# this list add the weight of all the vertex that were compared for later to get the smallest. ergo nearest neighbor
    distance_sum = 0

    for i in range(len(unvisited_list)):

        for n in unvisited_list:

            # the if will avoid added vertex that are already in the official route
            if n not in visi_list:
                #this method  will return the distance between two vertex
                distance = PackageDistance.getDistance_id(startVertex, n)
                #print("from", startVertex, "to", n, "distance", distance)
                weight_list.append([distance, n])

        # the minimam distance between two vertex is return as mini dis
        #this will get the smallest weight
        mini_dis = min(weight_list)
        id = mini_dis[1]
        min_distance = mini_dis[0]
        # this method will return the time be using the distance
        arrival_time = PackageDistance.playting_with_time2(arrival_time, min_distance)

        index = unvisited_list.index(id)
        # it will pop the id that had the smallest distance so it wont be reused
        unvisited_list.pop(index)
        # print(unvisited_list)
        startVertex = id
        visi_list.append(startVertex)
        #the weight list need to be cleared for a new loop and add new list of distance or the new vertex
        weight_list.clear()

        # the package count needs to be count to avoid added more the the limit of 16
        pack_count = pack_count + 1
        # the distance need to be added to avoid going over 140miles
        distance_sum = distance_sum + min_distance
        # the chosen vertex with the smallest weight will be added to the route list which is the official route list
        route_list.append(startVertex)

        # the the count equal 16 the hub distance is added to the total distance such as the start
        if pack_count == 16:
            hub_distance = PackageDistance.getDistance_id(0, startVertex)
            arrival_time = PackageDistance.playting_with_time2(arrival_time, hub_distance)
            temp_list = [[startVertex, arrival_time, pack_count, visi_list, route_list]]
            return temp_list

        # two time variable for the number nine special note
        time_a = datetime.timedelta(hours=10, minutes=20)
        time_b = datetime.timedelta(hours=11, minutes=20)
         # if time is between time_a and time_b then the package 9 will change the wrong address and be added univisted list agian
         # for a calculation again



        if ((arrival_time > time_a) & (arrival_time < time_b)):
            if (chosen_packList[0][3][0].count(9) < 1):
                h = pack_list.search_package(9)
                #print(h.distanceID)
                if h.distanceID != '20':
                    h.distanceID = '20'
                    h.address = '410 S State St'
                    h.city = 'Salt Lake City'
                    h.specialNotes = 'Address corrected'
                    #print("package id 9 had wrong address. It is added to the list again. ")
                    chosen_packList[0][3][0].append(9)
                    chosen_packList[0][3][1].append('20')
                    unvisited_list = chosen_packList[0][3][0]
                    id = 9
                    index = visi_list.index(id)
                    visi_list.pop(index)


    if ((pack_count < 16) & (len(visi_list) >= 40)):

        # this method will return the final list when all 40 package have.
        temp_list = [[startVertex, arrival_time, pack_count, visi_list,route_list]]
        return temp_list
    # this is where the recursion starts.
    if ((pack_count < 16)):
        # if one of the list are empty, it will go to the next one
        # it need to be in this order to deliver in time
        if chosen_packList[0][2][0] == []:
            #print("small window start")
            x = chosen_packList[0][1][0]
            # print("9am finished")
        if chosen_packList[0][1][0] == []:
            x = chosen_packList[0][0][0]
            #print("small window finished")
        if chosen_packList[0][0][0] == []:
            #print("10:30 finished")
            x = chosen_packList[0][3][0]
        if chosen_packList[0][3][0] == []:
            #print("EOD finished")
            x = chosen_packList[0][2][0]

        # the chosen x list will be added to the temp list and start the recursion with that list.
        temp_list = [[startVertex, arrival_time, pack_count, visi_list,route_list]]
        temp_list = NearestN(x, temp_list, chosen_packList)
        startVertex = temp_list[0][0]
        arrival_time = temp_list[0][1]
        visi_list = temp_list[0][3]
        pack_count = temp_list[0][2]


    temp_list = [[0, arrival_time, 0, visi_list,route_list]]
    return temp_list




# ---------------------------------------------------------------------------------------------------------------------




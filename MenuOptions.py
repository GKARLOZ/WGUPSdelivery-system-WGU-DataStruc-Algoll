import GreedyAlgo
import PackageDistance
import datetime
import NearestNeighborPath
import CSV


# this method will deliver all the package
# starting with this list as the starting point is the key to make all the package
# be delivered on time
def Deliver_all_packages():

    # the final list is the list with all the package inside a nested list
    final_list = []
    # this method will organize the package to their right list
    GreedyAlgo.greedyAlgo3(final_list)
    mileCount = 0


    t = datetime.timedelta(hours=8, minutes=0)
    packs = 0
    starting_id = 0
    visted_list = []
    route_list = []
    id_t_p_v_r = [[starting_id, t, packs, visted_list, route_list]]
    print(
        "\n\n=====================================  Truck number one =======================================================================\n\n")
    #this method will give the nearest neighbor path
    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    # statame will make the time start from 8am again
    id_t_p_v_r[0][1] = t
    # the method will load the truck and deliver the packages
    mileCount = mileCount + PackageDistance.Truck_on_Road(id_t_p_v_r, 1)
    # the route list need to be cleared for the next method but need to use the visited list
    id_t_p_v_r[0][4].clear()
    # the rest of the statement are the same as the top
    print(
        "\n\n=====================================  Truck number two =======================================================================\n\n")
    id_t_p_v_r[0][1] = datetime.timedelta(hours=8, minutes=0)
    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    id_t_p_v_r[0][1] = datetime.timedelta(hours=8, minutes=0)
    mileCount = mileCount + PackageDistance.Truck_on_Road(id_t_p_v_r, 2)
    id_t_p_v_r[0][4].clear()

    print(
        "\n\n=====================================  Truck number two (second round) =========================================================\n\n")
    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    id_t_p_v_r[0][1] = datetime.timedelta(hours=9, minutes=58)
    mileCount = mileCount + PackageDistance.Truck_on_Road(id_t_p_v_r, 2)
    print("Total Miles for both trucks: ", round(mileCount,2))

# this method is similar to the top method but modified to stop the
# process a certain time argo stop time
def pick_a_time(stop_time):

    # list of package hash table
    testing_hash = PackageDistance.package_hash

    # my list for the distances between addresses
    testing_graph = PackageDistance.address_graph

    # returns total number of destination in the file and adds them to the address_graph
    totalNumVertex = CSV.loadPackageDistanceData('WGUPS Distance Table.csv', testing_graph)

    # return the total number of packages in the file and saves them in to the package hash table as a packageDis object
    totalPacks = CSV.loadPackageDataWithDistance('PackageFile.csv', testing_hash, testing_graph)

    #print("\n\n=====================================  Truck number one ==========================================\n\n")

    final_list = []
    GreedyAlgo.greedyAlgo3(final_list)

    t = datetime.timedelta(hours=8, minutes=0)
    packs = 0
    starting_id = 0
    visted_list = []
    route_list = []
    id_t_p_v_r = [[starting_id, t, packs, visted_list, route_list]]

    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    id_t_p_v_r[0][1] = t
    if stop_time > id_t_p_v_r[0][1]:
     PackageDistance.Truck_on_Road_custTime(id_t_p_v_r, 1, stop_time)
    id_t_p_v_r[0][4].clear()

    #print("\n\n====================================  Truck number two ===========================================\n\n")
    id_t_p_v_r[0][1] = datetime.timedelta(hours=8, minutes=0)
    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    id_t_p_v_r[0][1] = datetime.timedelta(hours=8, minutes=0)

    if stop_time > id_t_p_v_r[0][1]:
      PackageDistance.Truck_on_Road_custTime(id_t_p_v_r, 2, stop_time)

    id_t_p_v_r[0][4].clear()

    #print( "\n\n=====================================  Truck number two (second round) =========================\n\n")
    ###
    ###
    ### import step in the process, this if statement will not update the number 9 package unless
    ## the stop time is over 1020am.
    over = datetime.timedelta(hours=10, minutes=20)
    if stop_time > over:
        id_t_p_v_r[0][1] = datetime.timedelta(hours=9, minutes=58)

    id_t_p_v_r = NearestNeighborPath.NearestN(final_list[0][2][0], id_t_p_v_r, final_list)
    id_t_p_v_r[0][1] = datetime.timedelta(hours=9, minutes=58)
    if stop_time > id_t_p_v_r[0][1]:
     PackageDistance.Truck_on_Road_custTime(id_t_p_v_r, 2, stop_time)

    for i in range(1,41):
        print(testing_hash.search_package(i))
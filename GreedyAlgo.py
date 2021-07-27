
# copy commented codes below and create these modules
import CSV
import PackageDistance
from Hash_Table import Hash_Table
import datetime
import NearestNeighborPath

def greedyAlgo3(x):
    small_window = [[], []]
    nine_o_five_list = [[], []]
    ten_thirty_list = [[], []]
    EOD_list = [[], []]
    added_to_a_list = []
    redo_EOD = []# this list will add the EOD package for later to reorganized them to the EOD_list
     # 40 packages in the list,
    for i in range(1,PackageDistance.totalPacks + 1):
        h = PackageDistance.package_hash.search_package(i)
        # word represents the specialnotes for every packaes
        word = h.specialNotes

        # These package id have to stay in the same route
        if ((h.ID == 13) | (h.ID == 19) | (h.ID == 15) | (h.ID == 14) | (h.ID == 16) | (h.ID == 20)):

            if ((h.ID not in added_to_a_list)):
                nine_o_five_list[0].append(h.ID)
                nine_o_five_list[1].append(h.distanceID)
                added_to_a_list.append(h.ID)
        # Just like the top, this package need to stay together but in a different list
        if ((h.ID == 32) | (h.ID == 31)):

            if ((h.ID not in added_to_a_list)):
                small_window[0].append(h.ID)
                small_window[1].append(h.distanceID)
                added_to_a_list.append(h.ID)

        if (h.ID == 28):
            ten_thirty_list[0].append(h.ID)
            ten_thirty_list[1].append(h.distanceID)
            added_to_a_list.append(h.ID)

        # if the special notes has the 9:05 in it then it will be added or the same distanceID
        if ((word.find('9:05 am') != -1) | ( h.distanceID in small_window[1])):
            if ((h.ID not in added_to_a_list) & (h.deliveryDeadline == "10:30 AM")):
                small_window[0].append(h.ID)
                small_window[1].append(h.distanceID)
                added_to_a_list.append(h.ID)

            if (h.ID not in added_to_a_list):
                nine_o_five_list[0].append(h.ID)
                nine_o_five_list[1].append(h.distanceID)
                added_to_a_list.append(h.ID)


        # if sdelivery deadline  equals 900am then it will be added or the same distance ID
        if ((h.deliveryDeadline == "9:00 AM")  | (h.distanceID in nine_o_five_list[1])):
            if (h.ID not in added_to_a_list):
                nine_o_five_list[0].append(h.ID)
                nine_o_five_list[1].append(h.distanceID)
                added_to_a_list.append(h.ID)
        # if the deliveryDead line is before 1030 it will be added
        if ((h.deliveryDeadline == "10:30 AM") | (h.distanceID in ten_thirty_list[1])):
            # some have the same dead line but need to arrive after 905
            if((word.find('9:05 am') == -1) & ( h.ID not in added_to_a_list)):
                    ten_thirty_list[0].append(h.ID)
                    ten_thirty_list[1].append(h.distanceID)
                    added_to_a_list.append(h.ID)

        # the rest are just EOD  and don't have a distance ID in any of them
        if ((h.deliveryDeadline == "EOD") & (word.find('9:05 am') == -1)):

            if (( h.ID not in added_to_a_list)):
                redo_EOD.append(h.ID)

    # the for loop will add the left EOD packages to the
    # rest of the list if they have the same distance ID
    for i in redo_EOD:

        h = PackageDistance.package_hash.search_package(i)
        # SMALL window list with the same distance ID
        if (h.distanceID in small_window[1]):
            if (h.ID not in added_to_a_list):
                small_window[0].append(h.ID)
                small_window[1].append(h.distanceID)
                added_to_a_list.append(h.ID)
        # nine am dead line with the same distance ID
        if (h.distanceID in nine_o_five_list[1]):
            if (h.ID not in added_to_a_list):
                nine_o_five_list[0].append(h.ID)
                nine_o_five_list[1].append(h.distanceID)
                added_to_a_list.append(h.ID)
        # ten thirty list with the same distace id
        if (h.distanceID in ten_thirty_list[1]):
            if (h.ID not in added_to_a_list):
                ten_thirty_list[0].append(h.ID)
                ten_thirty_list[1].append(h.distanceID)
                added_to_a_list.append(h.ID)
       # if they dont have any similar distance id it will be added to this one
        if ((h.ID not in added_to_a_list)):
            EOD_list[0].append(h.ID)
            EOD_list[1].append(h.distanceID)
            added_to_a_list.append(h.ID)


    added_to_a_list.sort()
    # print(added_to_a_list)

    x.append([ten_thirty_list, small_window, nine_o_five_list, EOD_list])






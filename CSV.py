
import csv

class packageDis:
    def __init__(self, ID, address, city, state, zip, deliveryDeadline, weightKilo, specialNotes, deliveryStatus, distanceID):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weightKilo = weightKilo
        self.specialNotes = specialNotes
        self.deliveryStatus = deliveryStatus
        self.distanceID = distanceID



    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deliveryDeadline, self.weightKilo, self.specialNotes,self.deliveryStatus,  self.distanceID)





# this method will store the packDIS objects to the hash table
# this method also will put the right vertex distanceID to the package that have the same address
def loadPackageDataWithDistance(fileName, myHash, D_List):
    totalPackages = 0
    with open(fileName) as PackageInfo:
        PackageData = csv.reader(PackageInfo, delimiter=',')
        next(PackageData)  # skip header
        for the_package in PackageData:
            pID = int(the_package[0])
            pAddress = the_package[1]
            pCity = the_package[2]
            pState = the_package[3]
            pZip = the_package[4]
            pDD = the_package[5]
            pKilo = the_package[6]
            pNote = the_package[7]
            pStatus = "at the hub"
            pDistance = 0

            #it is importante to note that the vertex distance table graph needs to be made first before
            # using this method
            # this will check every vertex and compare their address and if they match, it will add
            # the vertex id to the packages as a distanID
            packageFullAddress = "{}".format(" " + pAddress + "\n(" + pZip+ ")")
            for v in range(28):

                id_distance_list = D_List[v][0]

                #print("address from d list",D_List[v][2], "\np address", packageFullAddress )
                if D_List[v][2] == packageFullAddress:
                    #print(D_List[v][2], "   ", packageFullAddress)

                    #pDistance = D_List[v][0]
                    pDistance = D_List[v][0]

                    #print(pDistance, "   ", pID)
                    #print("MATCH-------------------------------------------------------------------------------", pDistance)



            # print(p)
             # package object
            p = packageDis(pID, pAddress, pCity, pState, pZip, pDD, pKilo, pNote, pStatus, pDistance)
            #print(p)
            # insert it into the hash table
            myHash.insert_package(pID, p)

            # Total amount of packages
            totalPackages += 1

    # Total amount of packages
    return totalPackages



# this method will store the wgu distance table to a graph
def loadPackageDistanceData(fileName,List):
    totalPackages = -1
    with open(fileName) as PackageInfo:
        PackageData = csv.reader(PackageInfo, delimiter=',')
        next(PackageData)  # skip header

        for i in PackageData:
            List.append(i)
            # Total amount of packages
            totalPackages += 1

    return totalPackages
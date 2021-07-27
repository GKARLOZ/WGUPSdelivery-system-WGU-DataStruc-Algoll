# Giancarlo Bustos

import CSV
import MenuOptions
import PackageDistance
import datetime


if __name__ == '__main__':
    print("\nGian's WGUPS program ")


    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get All Package Data")
        print("2. Find a Package with ID")
        print("3. Deliver all packages")
        print("4. Look at Package data at a certain time")
        print("5. Exit the Program")
        option = input("Chose an option (1,2,3 ,4 or 5): ")
        if option == "1":
            for i in range(1, 41):
                print(PackageDistance.package_hash.search_package(i))

        elif option == "2":
            ID = int(input("What is the ID of the package? "))
            print(PackageDistance.package_hash.search_package(ID))
        elif option == "3":
            MenuOptions.Deliver_all_packages()
        elif option == "4":

            human_put = int(input("Enter an hour(0-24):"))
            human_put2 = int(input("Enter the minutes(0-59):"))
            stop_time = datetime.timedelta(hours=human_put, minutes=human_put2)
            print(stop_time)
            MenuOptions.pick_a_time(stop_time)

        elif option == "5":
            isExit = False
        else:
            print("Wrong option, please try again!")



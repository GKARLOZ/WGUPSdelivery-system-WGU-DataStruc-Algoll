# WGU Postal Service Delivery System 

This program will display a menu for the user to pick from. 

        Options:
    1. Get All Package Data
    2. Find a Package with ID
    3. Deliver all packages
    4. Look at Package data at a certain time
    5. Exit the Program

The main goal of this program is to deliver the packages on time and follow the restrictions. In the CVS file, each package has certain restrictions that need to be met when delivering the packages. This program automatically creates a route so the drivers don't have to worry about the restrictions. The WGUPS routing program has a self-adjusting data structure that will store the package's data. This program has two algorithms that group the packages with similar restrictions and another algorithm to deliver the packages. The program won't have any issues delivering the packages if a new destination or package is added to the list because the data structures and algorithms are self-adjusting.

The program needs two CSV files that contain a list of packages with its data (PackageFile.csv) and another list of addresses (WGUPS Distance Table.csv). The list of packages is used to store the data in a hash table and the list of addresses is used to create a map.  



## Created with the following 
Software: IDE
PyCharm 2021.1.1 (Community Edition)
Build #PC-211.7142.13, built on April 21, 2021
Runtime version: 11.0.10+9-b1341.41 amd64
VM: Dynamic Code Evolution 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: G1 Young Generation, G1 Old Generation
Memory: 2020M
Cores: 8

## Visual Studio Code 
I didn't have any problems to run this program when using this version of VSC

Version: 1.70.2 
Node.js: 16.13.2
V8: 10.0.139.17-electron.0
OS: Windows_NT x64 10.0.22000


## Try it!
git clone https://github.com/GKARLOZ/WGUPSdelivery-system-WGU-DataStruc-Algoll.git

RUN CODE



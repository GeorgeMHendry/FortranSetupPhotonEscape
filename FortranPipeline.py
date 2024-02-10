import numpy as np
import os, sys



#This allows the user to enter the directory of the snapshots
Snapdir = input("Please enter the directory location of the snapshot files:\n")

#Sets the directory to this location
os.chdir(Snapdir)
#Creates a list with all the fils within the directory
files = os.listdir()

#This function defines a filter. Since the names of the snapshots are set in the parameter file for the code, these are known. 
def filter_files(file):
  #If the beginning of the file name starts with this then it will not be removed fro mthe filter
  if (file[0:10] == "disc_patch"):
    return True
  else:
    return False

#Filters the list using the filter_files function
filtered_files = np.sort(list(filter(filter_files,files)))

print("Compiled the list of files!")

#Asks the user for the resolution in the 3 dimensions.
xRes = str(input("Please enter the number of cells in the X-direction:\n"))
yRes = str(input("Please enter the number of cells in the Y-direction:\n"))
zRes = str(input("Please enter the number of cells in the Z-direction:\n"))

#Asks the user for the extent of the simulation in the 3 dimensions.
xLength = str(input("Please enter the extent in the  X-direction:\n"))
yLength = str(input("Please enter the extent in the  Y-direction:\n"))
zLength = str(input("Please enter the extent in the  Z-direction:\n"))


print("Opening file and writing to it.")
f = open("SnapshotData.params", "w")

f.write(str(len(filtered_files))+"\n")
f.write(xRes+"\n")
f.write(yRes+"\n")
f.write(zRes+"\n")
f.write(xLength+"\n")
f.write(yLength+"\n")
f.write(zLength+"\n")
for each in filtered_files:
  f.write(each+"\n")
f.close()
print("Finished writing to file.")




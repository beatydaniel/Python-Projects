import shutil
import os

#set where the source of the files are
source = '/Users/danis/OneDrive/Documents/GitHub/Python-Projects/File Transfer/FolderA/'
destination = '/Users/danis/OneDrive/Documents/GitHub/Python-Projects/File Transfer/FolderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

import os

def rename_files():
    # (1) get files names from a folder
    file_list = os.listdir("/Users/Alvin/GitHub/Python/Udacity-FS/prank")
    print(file_list)
    # (2) for each file, rename file name

rename_files()

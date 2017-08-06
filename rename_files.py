import os

def rename_files():
    # (1) get files names from a folder
    file_list = os.listdir("/Users/Alvin/GitHub/Python/Udacity-FS/prank")
    saved_path = os.getcwd()
    os.chdir("/Users/Alvin/GitHub/Python/Udacity-FS/prank")
    # (2) for each file, rename file name
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_name)
        print("The old name of the file is: " + file_name)
        print("The new name of the file is: " + new_name + "\n")
    # Change back the working directory
    os.chdir(saved_path)
    
rename_files()

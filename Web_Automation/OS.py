import os
# print(os.listdir()) # List all files and directories in the current directory
# CWD = os.getcwd() # Get the current working directory
# print("Current workind Dir", CWD)

# Create a new directory
new_dir = "New_Dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")

    #Rename Directory
    if not os.path.exists("Renamed_Dir"):
        os.rename(new_dir, "Renamed_Dir")
        print(f"Directory '{new_dir}' renamed to 'Renamed_Dir'.")

    # Remove Directory
    os.rmdir("Renamed_Dir")
    print(f"Directory 'Renamed_Dir' removed.")
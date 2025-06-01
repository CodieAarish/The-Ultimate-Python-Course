import os

# Specify the directory path
path = '/'  # Replace with your desired path

try:
    # Get the list of all files and directories
    dir_list = os.listdir(path)
    print(f"Contents of '{path}':")
    for item in dir_list:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
import os

path = '/'

try:
    dir_list = os.listdir(path)
    print(f"Contents of '{path}':")
    for item in dir_list:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")

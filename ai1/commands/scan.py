import os
from colorama import Fore, Style, init

init(autoreset=True)


def divider(length=70):
    for i in range(0, length):
        print(f"{Fore.GREEN}-", end="")
    print("\n")


def scan(path, tree=False):
    try:
        totalFiles = 0
        files = []
        for item in os.listdir(path):
            files.append(item)
            totalFiles += 1
        print(f"{Fore.BLUE}Total Files Found: {Fore.YELLOW}{totalFiles}")
        # Printing the files and folder with proper coloring
        divider()
        for file in files:
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                print(f"{Fore.CYAN}{file}", end=" ")
            elif os.path.isdir(full_path):
                print(f"{Fore.YELLOW}{file}", end=" ")
            else:  # Adding this because wanna know if there is a file which is not detected as file or folder
                print(f"{Fore.RED}Suspicious:{Fore.MAGENTA}{file}", end=" ")
        print("\n")

        if tree:
            os.system(f"tree {path}")
    except FileNotFoundError:
        print("Invalid Path")
    except NotADirectoryError:
        print("The given path is not of directory")

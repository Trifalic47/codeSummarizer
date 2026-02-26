import os


def scan(path):
    try:
        for item in os.listdir(path):
            print(item, end=" ")
        print()
    except FileNotFoundError:
        print("Invalid Path")

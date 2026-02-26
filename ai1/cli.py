import argparse
import ai1.commands.scan as scan


def cmd(command, path=None):
    if command == "scan":
        scan.scan(path)
    else:
        print("Working")


if __name__ == "__main__":
    pass

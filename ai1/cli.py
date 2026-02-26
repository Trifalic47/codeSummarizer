import argparse
import ai1.commands.scan as scan


def cmd(command, path=None, tree=False):
    if command == "scan":
        if tree:
            scan.scan(path, tree=True)
        else:
            scan.scan(path)
    else:
        print("Working")


if __name__ == "__main__":
    pass

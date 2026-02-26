import argparse
import ai1.cli as cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--command",
        type=str,
        help="Enter the tool's command to run",
        required=True,
    )

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Enter the path to scan",
    )
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Choose if you want to show the tree of the files",
    )

    # Parse ONLY ONCE
    args = parser.parse_args()

    tree = args.tree
    command = args.command
    path = args.path

    if command == "scan":
        if not path:
            print("Path is required for scan command")
        else:
            if args.tree:
                cli.cmd(command, path, tree=True)
            else:
                cli.cmd(command, path=path)
    else:
        print("Work going on..")

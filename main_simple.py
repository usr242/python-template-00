import argparse
import sys

"""
This template is for a very simple windows cli python script.
"""
script_description = f"{sys.argv[0]} snarfles the garthok with aplumb."


def get_args():
    parser = argparse.ArgumentParser(
        description=f""
    )
    parser.add_argument(
        '--test', help='test functionality'
    )
    arguments = parser.parse_args()
    return arguments


def main():
    # perform the function of the script
    args = get_args()
    print("main function stub")
    print(args)
    return 0


if __name__ == '__main__':
    main()

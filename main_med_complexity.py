import argparse
import configparser
import os
import sys

"""
This template is for a medium complexity windows cli python script.
Beyond this size/format, the script may be best broken into modules.
"""
script_description = f"snarfles the garthok with aplumb."


def get_args():
    # parser setup with some options referenced in comments see documentation for extended options
    parser = argparse.ArgumentParser(
        prog=f"{os.path.basename(sys.argv[0])}",  # restating default, but change/remove as desired
        # usage='This script is called with some arguments in order to do something.',
        # description=f"{script_description}",
        add_help=True,
        # allow_abbrev=True,
        # epilog="closing statements & wrap up"
    )
    # configuration for an opt/arg
    parser.add_argument('--test', dest='test_val', action='store', help='set test value')

    arguments = parser.parse_args()
    # return the parsed args in an object format.
    return arguments


def get_config():
    configuration = configparser.ConfigParser()
    configuration.read('configuration.ini')  # passed literal/static - but can be dynamic
    return configuration


def main():
    # perform the function of the script
    args = get_args()
    config = get_config()
    print("main function stub")
    print(f"print parsed arguments: {args}")
    print(f"print parsed configuration for boots: {config['DEFAULT']['boots']}")
    return 0


if __name__ == '__main__':
    main()

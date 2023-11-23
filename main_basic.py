import sys

"""
This template is for a very basic windows cli python script.
"""


def get_args():
    arg_count = len(sys.argv)
    for x in sys.argv:
        pass  # Do something with the arguments passed to the script
    return sys.argv


def main():
    # perform the function of the script
    arg_list = get_args()
    print("main function stub")
    return 0


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Sun 24 Jul 2022 07:19:20 AM EDT

This script is a rough template for basic python3 scripts that may grow into
larger format scripts or projects.
"""
import argparse
import configparser
import datetime
import sys

# some globals to make sharing user input easier
cli_arguments = None
configuration = None


def get_configuration():
    config = configparser.ConfigParser()
    config['DEFAULt'] = {
            'Keyword': 'buffalo'
            }
    return config


def argument_handler():
    argparser = argparse.ArgumentParser(description='a simple python starting point')
    argparser.add_argument('--test',type=str,help='testing option, requires a string')
    return argparser.parse_args()


def main():

    print(f"The current working directory is: {sys.path[0]}\n")

    if len(sys.argv) >= 2:
        for arg in sys.argv:
            print(f"arg: {arg}")
            print()

    current_time = datetime.datetime.today()
    print(f"{current_time}")
    

if __name__=='__main__':
    cli_arguments = argument_handler()
    configuration = get_configuration()
    main()
    exit()

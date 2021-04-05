"""
Processes the command line argument with the input and output file names to make sure all trigrams
with stop words are removed
Author – Nisha Choudhary
Date   – Sunday, April 4, 2021
"""

import argparse
import sys

def parse_args():
    """Parses the command line arguments provided by the user in order to only look at the trigrams
       without stop words
    
    Returns:
        str: The name of the input file with all of the trigrams, including ones with stop words
        str: The name of the output file to store all of the trigrams that don't have stop words
    """
    parser = argparse.ArgumentParser(description = "Takes in the input and the output file names")
    parser.add_argument("-i", "--input", type = str, default = None, metavar = "",\
        help = "the name of the input file preceded by its relative path (if needed)")
    parser.add_argument("-o", "--output", type = str, default = None, metavar = "",\
        help = "the name of the output file preceded by its relative path (if needed)")
    parser.add_argument("-v", "--verb", type = str, default = None, metavar = "",\
        help = "the main verb being looked at")
    arguments = parser.parse_args()
    
    if(arguments.input == None):
        # no input path + file name was specified
        print("Please enter the name of the input file.")
        parser.print_help()
        sys.exit()
    
    if(arguments.output == None):
        # no output path + file name was specified
        print("Please enter the name of the output file.")
        parser.print_help()
        sys.exit()
    
    if(arguments.verb == None):
        # the verb wasn't specified
        print("Please enter the main verb to be looked at.")
        parser.print_help()
        sys.exit()
    
    if(arguments.input == arguments.output):
        print("Please specify a different name and path for the input and the ouput.")
        parser.print_help()
        sys.exit()
    
    return arguments.input, arguments.output, arguments.verb

if __name__ == "__main__":
    input, output, verb = parse_args()
    print(input, output, verb)
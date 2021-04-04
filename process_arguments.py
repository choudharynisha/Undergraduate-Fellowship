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
       without stopwords
    
    Returns:
        str: The name of the input file with all of the trigrams, including ones with stop words
        str: The name of the output file to store all of the trigrams that don't have stop words
    """
    parser = argparse.ArgumentParser(description = "Takes in the input and the output file names")
    parser.add_argument("-i", "--input", type = str, help = "the name of the input file",\
        default = None, metavar = "")
    parser.add_argument("-o", "--output", type = str, help = "the name of the output file",\
        default = None, metavar = "")
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
    
    if(arguments.input == arguments.output):
        print("Please specify a different name and path for the input and the ouput.")
        parser.print_help()
        sys.exit()
    
    return arguments.input, arguments.output

if __name__ == "__main__":
    input, output = parse_args()
    print(input, output)
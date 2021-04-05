"""
All functions for reading in and writing to text files (.txt)
Author – Nisha Choudhary
Date   – Sunday, April 4, 2021
"""

import identify_arguments

def read_in_data(filename, verb):
    """Reads in and saves the lines from the file where the trigrams have the specified verb
    
    Args:
        filename (str): The name of the input file, preceded by the relative path (if needed)
        verb (str): The specified verb to look for as the second token in the trigrams
    
    Returns:
        list: The lines of trigrams with their corresponding frequency with the specified verb in
        the middle of the trigram
    """
    lines = []
    
    with open(filename) as file:
        next_line = file.readline()
        next_line = file.readline()
        next_line = file.readline()
        next_line = file.readline()
        next_line = file.readline()
        tokens = next_line.split()
        
        while True:
            lines.append(next_line)
            next_line = file.readline()
            tokens = next_line.split()
            
            if(tokens[1] != verb):
                break
    
    print(len(lines))
    return lines

if __name__ == "__main__":
    input, output, verb = identify_arguments.parse_args()
    print(input, output, verb)
    trigrams_and_frequency = read_in_data(input, verb)
    print(len(trigrams_and_frequency))
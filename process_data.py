"""
All functions for reading in and writing to text files (.txt)
Author – Nisha Choudhary
Date   – Sunday, April 4, 2021
"""

import identify_arguments
from nltk.corpus import stopwords
from operator import itemgetter

def ignore_stop_words(trigrams_and_frequency):
    """Filters out the trigrams that have a stop word in the third token of the trigram
    
    Args:
        trigrams_and_frequency (list): The list of trigrams with their corresponding frequencies
        
    Returns:
        list: The subset of trigrams_and_frequency where none of the trigrams contain a stop word
         as the third token
    """
    filtered_trigrams = []
    
    for line in trigrams_and_frequency:
        tokens = line.split() # default = splity by spaces
        
        if tokens[2] not in set(stopwords.words("english")):
            # the third token in the trigram is not a stop word
            filtered_trigrams.append(line)
        
    return filtered_trigrams

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
        # the first line with the specified verb in the middle of the trigram is the fifth line of
        # the file
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
                # terminate / break out of the loop once the verb is no longer the specified verb
                break
    
    file.close()
    return lines

def sort(trigrams_and_frequency):
    split = []
    ordered = []
    
    for line in trigrams_and_frequency:
        tokens = line.split()
        trigram = tokens[0] + " " + tokens[1] + " " + tokens[2]
        row = [trigram, tokens[3]]
        split.append(row)
    
    split.sort(key = lambda x: x[1])
    
    for row in split:
        line = row[0] + " " + row[1] + "\n"
        ordered.append(line)
    
    return ordered

def write_to_file(filename, trigrams_and_frequency):
    """Takes the filtered list of trigrams and their corresponding frequencies and writes it to a 
    new text file
    
    Args:
        filename (str): The name of the file to create and write to with the relative path preceding 
        the name (if needed)
        trigrams_and_frequency (list): The filtered list of trigrams and their corresponding 
        frequencies
    """
    file = open(filename, "w")
    
    for line in trigrams_and_frequency:
        file.write(line)
    
    file.close()

if __name__ == "__main__":
    input, output, verb = identify_arguments.parse_args()
    trigrams_and_frequency = read_in_data(input, verb)
    print(len(trigrams_and_frequency))
    filtered_trigrams = ignore_stop_words(trigrams_and_frequency)
    print(len(filtered_trigrams))
    sorted = sort(filtered_trigrams)
    print(len(sorted))
    write_to_file(output, sorted)
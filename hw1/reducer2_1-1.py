#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

# Function to read mapper output and return key-value pairs
def read_mapper_output(input, separator='\t'):
    for line in input:
        # Strip leading/trailing whitespace
        line = line.strip()
        if line:  # Skip any empty lines
            yield line.split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["", ""] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for _, count in group)
            print(f'{current_word}{separator}{total_count}')
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()

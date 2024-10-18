#!/usr/bin/env python3
import sys
from heapq import heappop, heappush

def read_input(input, separator='\t'):
    for line in input:
        # Remove any leading/tailing space
        line = line.strip()
        if line:  # skip any empty lines
            yield line.split(separator, 2)

def main(separator='\t'):
    # Keep a min heap of (count, word)
    desc_count = []
    # Read data
    data = read_input(sys.stdin, separator)
    # For each row of data
    for d in data:
        # Ignore d[0] - temp key
        # Insert into the heap
        count, word = int(d[1]), d[2]
        heappush(desc_count, (count, word))
    # Index starts at 1
    index = 1
    while desc_count:
        # Get the min(max in count since we negated the integer in mapper) 
        # and print with index 
        min_word = heappop(desc_count)[1]
        print(f'{index}{separator}{min_word}')
        index += 1
    
if __name__ == "__main__":
    main()
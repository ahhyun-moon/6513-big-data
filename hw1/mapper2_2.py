#!/usr/bin/env python3
import sys

def main(separator='\t'):
    for line in sys.stdin:
        # Remove any leading/tailing space
        line = line.strip()
        if line:  # skip any empty lines
            word, count = line.split(separator, 1)
            # Convert the count to negative integer for
            # using heapq (minheap) in reducer for descending order
            # Print with '_' - temporary key to force key &
            # values into a single reducer
            print(f'_{separator}{-int(count)}{separator}{word}')
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import sys
from heapq import heappop, heappush, heapify

def read_input(input, separator='\t'):
    for line in input:
        # Remove any leading/tailing space
        line = line.strip()
        if line:  # skip any empty lines
            yield line.split(separator, 1)

def main(separator='\t'):
    # Keep a heap of local top k
    local_top_heap = []
    k = 10
    # Read data
    data = read_input(sys.stdin, separator)
    # For each row of data:
    for d in data:
        word, count = d[0], int(d[1])
        # When items in local top heap is less than K
        # Insert the (count, word)
        if len(local_top_heap) < k:
            heappush(local_top_heap, (count, word))
        else:
        # When items in local top heap is >= K
        # Insert the count into the heap when 
        # the count is greater than the min of heap
            if local_top_heap[0][0] < count:
                heappop(local_top_heap) # Remove the min
                heappush(local_top_heap, (count, word)) # Insert the count
    # Print k outputs in local top heap (not sorted yet)
    for item in local_top_heap:
        word_count = f'{item[1]}{separator}{item[0]}'
        # Print with '_' - temporary key to force key &
        # values into a single reducer for final top k
        print(f'_{separator}{word_count}')
if __name__ == "__main__":
    main()
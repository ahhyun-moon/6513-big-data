#!/usr/bin/env python3
import sys
from heapq import heappop, heappush, heapify

def read_input(input, separator='\t'):
    for line in input:
        # Remove any leading/tailing space
        line = line.strip()
        if line:  # skip any empty lines
            yield line.split(separator, 2)

def main(separator='\t'):
    # Keep a heap of local top k
    top_heap = []
    k = 10
    # Read data
    data = read_input(sys.stdin, separator)
    # For each row of data:
    for d in data:
        # Ignore d[0] - temp key
        # Store count and word into the heap when less than k items
        count, word = int(d[2]), d[1]
        if len(top_heap) < k:
            heappush(top_heap, (count, word))
        # When the heap already has k items,
        # Remove the min and insert the (count, word) if count > min
        else:
            if top_heap[0][0] < count:
                heappop(top_heap)
                heappush(top_heap, (count, word))
    # Pop each min and add onto the top k list in descending order
    top_k = []
    while top_heap:
        min_count, min_word = heappop(top_heap)
        top_k = [f'{min_word}{separator}{min_count}'] + top_k
    print("\n".join(top_k))
    
if __name__ == "__main__":
    main()
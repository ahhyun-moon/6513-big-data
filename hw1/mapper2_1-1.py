#!/usr/bin/env python3
import re
import sys

def read_input(input):
    for line in input:
         # Replace with space for chars other than assigned ones
        line = re.sub(r'([^A-Za-z0-9.,\-\(\)\[\]])', ' ', line)
         # Added space before and after punctuations for split (tokenization)
        line = re.sub(r'([.,\-()[\]])', r' \1 ', line)
         # Remove any leading/tailing space
        line = line.strip()
        if line:  # skip any empty lines
            yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    # Added trivial count 1 to each word
    for words in data:
        for word in words:
            print(f'{word}{separator}1')

if __name__ == "__main__":
    main()

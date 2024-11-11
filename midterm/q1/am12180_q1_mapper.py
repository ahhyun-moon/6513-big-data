#!/usr/bin/env python3
import sys
import random

def main(separator='\t'):
    bucket_size = 900  # Desired reservoir size
    bucket = []
    curr_count = 0
    for line in sys.stdin:
        line = line.strip()
        curr_count += 1
        # Fill the bucket until we reach bucket_size
        if curr_count <= bucket_size:
            bucket.append(line)
        else:
            # Randomly select a number between 0 and current count - 1
            # If the number is within the bucket size, replace the item at that index
            random_num = random.randint(0, curr_count - 1)
            if random_num < bucket_size:
                bucket[random_num] = line

    # Output each item in the bucket with a key for the reducer
    for item in bucket:
        print(f"1{separator}{item}")

if __name__ == "__main__":
    main()

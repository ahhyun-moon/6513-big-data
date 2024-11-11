#!/usr/bin/env python3
import sys
import random

def main(separator='\t'):
    bucket_size = 900  # Final reservoir size
    bucket = []
    curr_count = 0
    for data in sys.stdin:
        data = data.strip()
        if separator in data:
            _, line = data.split(separator, 1)
            line = line.strip()
            curr_count += 1
            # Fill the bucket until we reach bucket_size
            if curr_count <= bucket_size:
                bucket.append(line)
            else:
                # Randomly select an index to replace if needed
                random_num = random.randint(0, curr_count - 1)
                if random_num < bucket_size:
                    bucket[random_num] = line

    # Output each item in the final reservoir
    print("\n".join(bucket))

if __name__ == "__main__":
    main()

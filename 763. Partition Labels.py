#https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Track the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Step 2: Initialize variables
        partitions = []
        start = 0  # Start of the current partition
        end = 0    # End of the current partition

        # Step 3: Traverse the string to create partitions
        for i, char in enumerate(s):
            # Update the end of the current partition
            end = max(end, last_occurrence[char])
            
            # If the current index reaches the end of the partition
            if i == end:
                # Add the size of the partition to the result
                partitions.append(end - start + 1)
                # Move the start to the next partition
                start = i + 1

        return partitions

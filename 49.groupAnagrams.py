from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dictionary where each key maps to a list
        # This will store groups of anagrams under the same key
        res = defaultdict(list)

        # Loop through each string in the input list
        for s in strs:
            # Create a list of 26 zeros (for each letter a–z)
            # Each index represents the count of a particular character
            count = [0] * 26

            # Count how many times each character appears in the string
            for c in s:
                # ord(c) gives ASCII value, ord('a') aligns 'a' to index 0
                # Example: 'a'→0, 'b'→1, ..., 'z'→25
                count[ord(c) - ord('a')] += 1

            # Convert list to tuple since lists can't be used as dictionary keys
            # All anagrams will have the same tuple key (same letter counts)
            res[tuple(count)].append(s)

        # Return only the grouped lists of anagrams
        # res.values() gives all the lists of words grouped by anagram pattern
        return list(res.values())

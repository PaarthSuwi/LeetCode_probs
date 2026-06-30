# ============================================================
# LeetCode 1207 - Unique Number of Occurrences
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an array of integers arr, return true if the number of
# occurrences of each value in the array is unique, or false otherwise.
#
# Example 1:
#   Input:  arr = [1,2,2,1,1,3]
#   Output: True
#   Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time.
#                All occurrence counts (3, 2, 1) are distinct.
#
# Example 2:
#   Input:  arr = [1,2]
#   Output: False  (both appear 1 time)
#
# Constraints:
#   - 1 <= arr.length <= 1000
#   - -1000 <= arr[i] <= 1000
#
# ============================================================
# THEORY / APPROACH:
# Count the frequency of each element using a hash map (Counter).
# Then check if all frequency values are distinct by comparing the
# length of the frequency dict to the length of a set of its values.
# If they differ, some frequencies repeat -> return False.
#
# Time Complexity: O(n) -- single pass to count + set creation
# Space Complexity: O(n) -- frequency map and set
# ============================================================

from collections import Counter
from typing import List

class Solution:
      def uniqueOccurrences(self, arr: List[int]) -> bool:
                freq = Counter(arr)
                # All occurrence counts must be unique
                return len(freq) == len(set(freq.values()))

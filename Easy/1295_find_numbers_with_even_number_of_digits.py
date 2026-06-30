# ============================================================
# LeetCode 1295 - Find Numbers with Even Number of Digits
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an array nums of integers, return how many of them contain
# an even number of digits.
#
# Example 1:
#   Input:  nums = [12,345,2,6,7896]
#   Output: 2   (12 has 2 digits, 7896 has 4 digits)
#
# Example 2:
#   Input:  nums = [555,901,482,1771]
#   Output: 1   (1771 has 4 digits)
#
# Constraints:
#   - 1 <= nums.length <= 500
#   - 1 <= nums[i] <= 10^5
#
# ============================================================
# THEORY / APPROACH:
# Convert each number to a string and check if its length is even.
# This avoids logarithm edge cases and is the most Pythonic approach.
# An equivalent approach: compare against digit-boundary thresholds
# (10, 1000, 100000) to classify numbers by digit count parity.
#
# Time Complexity: O(n) -- single scan; digit conversion is O(1) since
#                 numbers are bounded to at most 6 digits.
# Space Complexity: O(1) -- only a counter variable
# ============================================================

from typing import List

class Solution:
      def findNumbers(self, nums: List[int]) -> int:
                return sum(1 for num in nums if len(str(num)) % 2 == 0)

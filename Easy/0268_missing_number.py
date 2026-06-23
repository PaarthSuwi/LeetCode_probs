# ============================================================
# LeetCode 268 - Missing Number
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Example:
#   Input:  nums = [3,0,1]    Output: 2
#   Input:  nums = [9,6,4,2,3,5,7,0,1]   Output: 8
#
# Constraints:
#   - n == nums.length
#   - 1 <= n <= 10^4
#   - 0 <= nums[i] <= n
#   - All values of nums are unique.
#
# ============================================================
# THEORY / APPROACH:
# Gauss formula: sum of 0..n = n*(n+1)/2.
# The missing number = expected_sum - actual_sum.
# Single pass, O(1) space. No sorting, no hash set needed.
#
# Alternative: XOR approach (XOR all indices and values, missing = result).
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)

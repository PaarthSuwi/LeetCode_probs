# ============================================================
# LeetCode 724 - Find Pivot Index
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# Given an array of integers nums, return the pivot index.
# The pivot index is where the sum of all numbers to the left of the
# index is equal to the sum of all numbers to the right.
# If no pivot exists, return -1. If multiple pivots exist, return the leftmost.
#
# Example:
#   Input:  nums = [1,7,3,6,5,6]   Output: 3
#            (left sum = 1+7+3 = 11, right sum = 5+6 = 11)
#   Input:  nums = [1,2,3]         Output: -1
#
# Constraints:
#   - 1 <= nums.length <= 10^4
#   - -1000 <= nums[i] <= 1000
#
# ============================================================
# THEORY / APPROACH:
# Prefix sum technique. Compute total sum once.
# Iterate: maintain left_sum. At index i: right_sum = total - left_sum - nums[i].
# If left_sum == right_sum, return i.
# Update left_sum += nums[i] and continue.
#
# Prefix sums are heavily used in robotics for cumulative sensor readings,
# range queries on IMU/encoder data, and sliding window computations.
#
# Time Complexity:  O(n)  — two passes (one for sum, one for pivot)
# Space Complexity: O(1)
# ============================================================

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1

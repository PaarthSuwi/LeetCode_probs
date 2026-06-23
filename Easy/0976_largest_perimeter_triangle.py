# ============================================================
# LeetCode 976 - Largest Perimeter Triangle
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an integer array nums, return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths.
# If impossible, return 0.
# Triangle inequality: sum of two shorter sides > longest side.
#
# Example:
#   Input:  nums = [2,1,2]    Output: 5
#   Input:  nums = [1,2,1]    Output: 0
#
# Constraints:
#   - 3 <= nums.length <= 10^4
#   - 1 <= nums[i] <= 10^6
#
# ============================================================
# THEORY / APPROACH:
# Sort in descending order. For each consecutive triple (a >= b >= c),
# check if b + c > a (triangle inequality). If true, return a + b + c.
# Due to sorting, the first valid triple gives the largest perimeter.
# We only need to check triples where a is the largest side.
#
# Time Complexity:  O(n log n)  — sorting dominates
# Space Complexity: O(1)        — or O(n) for sort depending on language
# ============================================================

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:
                return a + b + c
        return 0

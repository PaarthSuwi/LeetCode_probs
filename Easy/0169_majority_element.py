# ============================================================
# LeetCode 169 - Majority Element
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n/2 times.
# You may assume the majority element always exists in the array.
#
# Example:
#   Input:  nums = [3,2,3]
#   Output: 3
#   Input:  nums = [2,2,1,1,1,2,2]
#   Output: 2
#
# Constraints:
#   - n == nums.length
#   - 1 <= n <= 5 * 10^4
#   - -10^9 <= nums[i] <= 10^9
#
# ============================================================
# THEORY / APPROACH:
# Boyer-Moore Voting Algorithm. Maintain a candidate and a count.
# If count is 0, set current element as new candidate.
# If current element matches candidate, increment count; else decrement.
# The majority element will survive as the final candidate.
#
# Time Complexity:  O(n)  — single pass
# Space Complexity: O(1)  — only two variables
# ============================================================

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

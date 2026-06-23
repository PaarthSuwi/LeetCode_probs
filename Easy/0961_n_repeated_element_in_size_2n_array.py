# ============================================================
# LeetCode 961 - N-Repeated Element in Size 2N Array
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are given an integer array nums with length 2 * n. The array
# contains n + 1 unique elements with exactly one element repeated n times.
# Return the element that is repeated n times.
#
# Example:
#   Input:  nums = [1,2,3,3]    Output: 3
#   Input:  nums = [5,1,5,2,5,3,5,4]   Output: 5
#
# Constraints:
#   - 2 <= n <= 5000
#   - nums.length == 2 * n
#   - 0 <= nums[i] <= 10^4
#   - nums contains exactly n + 1 unique elements with one repeated n times.
#
# ============================================================
# THEORY / APPROACH:
# Observation: with 2n elements and one repeated n times, pigeonhole
# principle guarantees that among any 3 consecutive elements, two must
# be the repeated one. Check pairs at distance 1 and 2. If neither,
# check first and last.
#
# Alternative: use a set, return when a duplicate is found.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — constant-distance check approach
# ============================================================

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

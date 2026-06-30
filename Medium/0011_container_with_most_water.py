# ============================================================
# LeetCode 11 - Container With Most Water
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# You are given an integer array height of length n. There are n
# vertical lines drawn such that the two endpoints of the i-th line
# are (i, 0) and (i, height[i]). Find two lines that together with
# the x-axis form a container such that the container holds the most
# water. Return the maximum amount of water a container can store.
#
# Example 1:
#   Input:  height = [1,8,6,2,5,4,8,3,7]
#   Output: 49   (lines at index 1 and 8: min(8,7) * 7 = 49)
#
# Example 2:
#   Input:  height = [1,1]
#   Output: 1
#
# Constraints:
#   - n == height.length
#   - 2 <= n <= 10^5
#   - 0 <= height[i] <= 10^4
#
# ============================================================
# THEORY / APPROACH:
# Two-pointer technique: start with left=0 and right=n-1 (widest span).
# Water = min(height[left], height[right]) * (right - left).
# Move the pointer at the shorter wall inward: the width always
# decreases, so we only win by finding a taller partner.
# Continue until the pointers meet, tracking the max area.
#
# Time Complexity: O(n) -- single pass with two pointers
# Space Complexity: O(1) -- only two pointer variables
# ============================================================

from typing import List

class Solution:
      def maxArea(self, height: List[int]) -> int:
                left, right = 0, len(height) - 1
                max_water = 0
                while left < right:
                              water = min(height[left], height[right]) * (right - left)
                              max_water = max(max_water, water)
                              if height[left] <= height[right]:
                                                left += 1
else:
                right -= 1
          return max_water

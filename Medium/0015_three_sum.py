# ============================================================
# LeetCode 15 - 3Sum
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i, j, k are distinct and
# nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.
#
# Example 1:
#   Input:  nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
#   Input:  nums = [0,0,0]
#   Output: [[0,0,0]]
#
# Constraints:
#   - 3 <= nums.length <= 3000
#   - -10^5 <= nums[i] <= 10^5
#
# ============================================================
# THEORY / APPROACH:
# Sort first, then fix the leftmost element nums[i] and use
# two pointers (left=i+1, right=n-1) to find pairs summing to
# -nums[i]. Skip duplicates at each level to avoid repeated triplets.
#
# Time Complexity: O(n^2) -- O(n log n) sort + O(n) two-pointer per i
# Space Complexity: O(1) -- sort is in-place, output not counted
# ============================================================

from typing import List

class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
                nums.sort()
                result = []
                n = len(nums)
                for i in range(n - 2):
                              if i > 0 and nums[i] == nums[i - 1]:
                                                continue
                                            if nums[i] > 0:
                                                              break
                                                          left, right = i + 1, n - 1
                              target = -nums[i]
                              while left < right:
                                                s = nums[left] + nums[right]
                                                if s == target:
                                                                      result.append([nums[i], nums[left], nums[right]])
                                                                      while left < right and nums[left] == nums[left + 1]:
                                                                                                left += 1
                                                                                            while left < right and nums[right] == nums[right - 1]:
                                                                                                                      right -= 1
                                                                                                                  left += 1
                                                                      right -= 1
elif s < target:
                    left += 1
else:
                    right -= 1
          return result

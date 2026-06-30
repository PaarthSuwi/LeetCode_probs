# ============================================================
# LeetCode 56 - Merge Intervals
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the
# non-overlapping intervals that cover all intervals in the input.
#
# Example 1:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
# Example 2:
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]   (touching intervals also merge)
#
# Constraints:
#   - 1 <= intervals.length <= 10^4
#   - 0 <= starti <= endi <= 10^4
#
# ============================================================
# THEORY / APPROACH:
# Sort intervals by start time. Then scan greedily:
#   - Overlap (current.start <= last.end): extend last.end.
#   - No overlap: append current as a new interval.
#
# Time Complexity: O(n log n) -- sort + O(n) merge pass
# Space Complexity: O(n) -- output list
# ============================================================

from typing import List

class Solution:
      def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                intervals.sort(key=lambda x: x[0])
                merged = []
                for start, end in intervals:
                              if merged and merged[-1][1] >= start:
                                                merged[-1][1] = max(merged[-1][1], end)
else:
                merged.append([start, end])
          return merged

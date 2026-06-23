# ============================================================
# LeetCode 119 - Pascal's Triangle II
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an integer rowIndex, return the rowIndex-th (0-indexed) row
# of Pascal's triangle using only O(rowIndex) extra space.
#
# Example:
#   Input:  rowIndex = 3
#   Output: [1,3,3,1]
#   Input:  rowIndex = 0
#   Output: [1]
#
# Constraints:
#   - 0 <= rowIndex <= 33
#
# ============================================================
# THEORY / APPROACH:
# Initialize a row of (rowIndex+1) ones. For each row from 2 to rowIndex,
# iterate from right to left updating: row[j] += row[j-1].
# Updating right-to-left avoids overwriting values we still need.
# This uses O(n) space and builds the row in-place.
#
# Each element: C(n,k) = C(n-1,k-1) + C(n-1,k)
#
# Time Complexity:  O(n^2)  — n = rowIndex
# Space Complexity: O(n)    — single row stored
# ============================================================

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row

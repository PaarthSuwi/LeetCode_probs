# ============================================================
# LeetCode 1937 - Maximum Number of Points with Cost
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# You are given an m x n integer matrix points. Points gained by selecting
# one cell per row, and transitioning from cell (r, c1) to (r+1, c2) costs
# |c1 - c2|. Maximize: sum of points[r][c] - transition costs.
#
# Example:
#   Input:  points = [[1,2,3],[1,5,1],[3,1,1]]
#   Output: 9  (select (0,2), (1,1), (2,0) = 3+5+3-|2-1|-|1-0| = 9)
#
# Constraints:
#   - m == points.length, n == points[r].length
#   - 1 <= m, n <= 10^5
#   - 0 <= points[r][c] <= 10^5
#
# ============================================================
# THEORY / APPROACH:
# DP with left and right sweeps to avoid O(n^2) per row.
# dp[j] = max points achievable at column j in current row.
# Left sweep: max(dp[j], left_max - j) where left_max accumulates dp[j] + j.
# Right sweep: similar but from right (dp[j] + n-1-j from right).
# Combine both sweeps with current row's points.
#
# Time Complexity:  O(m * n)  — two sweeps per row
# Space Complexity: O(n)      — single DP array
# ============================================================

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for r in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j-1] - 1, dp[j])

            right[n-1] = dp[n-1]
            for j in range(n-2, -1, -1):
                right[j] = max(right[j+1] - 1, dp[j])

            dp = [points[r][j] + max(left[j], right[j]) for j in range(n)]

        return max(dp)

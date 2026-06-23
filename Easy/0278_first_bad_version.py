# ============================================================
# LeetCode 278 - First Bad Version
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are a product manager and leading a team to develop a new product.
# Given n versions [1, 2, ..., n], find the first bad version.
# isBadVersion(version) API tells whether a version is bad.
# All versions after a bad version are also bad. Minimize API calls.
#
# Example:
#   Input:  n = 5, bad = 4
#   Output: 4  (versions 4 and 5 are bad)
#
# Constraints:
#   - 1 <= bad <= n <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# Binary search. If mid is bad, the first bad is in [lo, mid].
# If mid is good, the first bad is in [mid+1, hi].
# Use lo = mid (not mid+1) when mid is bad, to avoid missing it.
#
# Key: use mid = lo + (hi - lo) // 2 to avoid integer overflow.
#
# Time Complexity:  O(log n)  — binary search
# Space Complexity: O(1)
# ============================================================

def isBadVersion(version: int) -> bool:
    pass  # Provided by the problem's API

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

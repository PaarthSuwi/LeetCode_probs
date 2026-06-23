# ============================================================
# LeetCode 374 - Guess Number Higher or Lower
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# We pick a number from 1 to n. You must guess which number.
# API guess(num) returns: -1 (pick < num), 1 (pick > num), 0 (correct).
# Return the number you picked.
#
# Example:
#   Input:  n = 10, pick = 6
#   Output: 6
#
# Constraints:
#   - 1 <= n <= 2^31 - 1
#   - 1 <= pick <= n
#
# ============================================================
# THEORY / APPROACH:
# Binary search. At each step call guess(mid):
#   - If 0: found it, return mid
#   - If -1: answer is lower, search [lo, mid-1]
#   - If 1: answer is higher, search [mid+1, hi]
#
# Use mid = lo + (hi - lo) // 2 to prevent overflow.
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

def guess(num: int) -> int:
    pass  # Provided by API

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

# ============================================================
# LeetCode 231 - Power of Two
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an integer n, return true if it is a power of two.
# An integer n is a power of two if there exists an integer x such that n == 2^x.
#
# Example:
#   Input:  n = 1    Output: True  (2^0 = 1)
#   Input:  n = 16   Output: True  (2^4 = 16)
#   Input:  n = 3    Output: False
#
# Constraints:
#   - -2^31 <= n <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# Powers of two have exactly one set bit in binary. So n & (n-1) == 0
# removes that single set bit, leaving 0. Also n must be positive.
#
# Example: 8 = 1000, 8-1 = 0111, 8 & 7 = 0000 (True)
#          6 = 0110, 6-1 = 0101, 6 & 5 = 0100 (False, not zero)
#
# Relevance: power-of-two checks appear in memory alignment and
# buffer sizing in embedded/robotics systems.
#
# Time Complexity:  O(1)
# Space Complexity: O(1)
# ============================================================

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

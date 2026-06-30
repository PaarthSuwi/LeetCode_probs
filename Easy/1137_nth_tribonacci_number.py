——# ============================================================
# LeetCode 1137 - N-th Tribonacci Number
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# The Tribonacci sequence T(n) is defined as follows:
#   T(0) = 0, T(1) = 1, T(2) = 1
#   T(n+3) = T(n) + T(n+1) + T(n+2)  for n >= 0
# Given n, return the value of T(n).
#
# Example 1:
#   Input:  n = 4
#   Output: 4    (T: 0,1,1,2,4)
#
# Example 2:
#   Input:  n = 25
#   Output: 1389537
#
# Constraints:
#   - 0 <= n <= 37
#   - The answer is guaranteed to fit within a 32-bit integer.
#
# ============================================================
# THEORY / APPROACH:
# Use iterative bottom-up DP with three rolling variables (O(1) space).
# We track the last three Tribonacci values and slide the window forward.
#
# Base cases: T(0)=0, T(1)=1, T(2)=1 are handled directly.
# For n >= 3, each new value = sum of previous three.
#
# Time Complexity: O(n) -- single loop from 3 to n
# Space Complexity: O(1) -- only three integer variables
# ============================================================

class Solution:
      def tribonacci(self, n: int) -> int:
                if n == 0:
                              return 0
                          if n <= 2:
                                        return 1
                                    a, b, c = 0, 1, 1
                for _ in range(3, n + 1):
                              a, b, c = b, c, a + b + c
                          return c

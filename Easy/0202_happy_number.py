# ============================================================
# LeetCode 202 - Happy Number
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# A happy number is defined by:
#   1. Starting with any positive integer, replace the number by the
#      sum of squares of its digits.
#   2. Repeat until the number equals 1 (happy) or loops endlessly (not happy).
# Return True if n is a happy number.
#
# Example:
#   Input:  n = 19
#   Output: True  (19->82->68->100->1)
#   Input:  n = 2
#   Output: False
#
# Constraints:
#   - 1 <= n <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# Use Floyd's cycle detection (slow/fast pointers) on the sequence.
# If the sequence reaches 1 => happy. If slow and fast meet at != 1 => cycle.
# Alternative: use a set to detect cycles.
#
# Time Complexity:  O(log n)  — sum of digit squares reduces n quickly
# Space Complexity: O(1)  — Floyd's; O(log n) with set approach
# ============================================================

class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit * digit
            return total

        slow, fast = n, sum_of_squares(n)
        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
        return fast == 1

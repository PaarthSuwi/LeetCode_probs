# ============================================================
# LeetCode 168 - Excel Sheet Column Title
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an integer columnNumber, return its corresponding column title
# as it appears in an Excel spreadsheet.
#   1 -> A, 2 -> B, ..., 26 -> Z, 27 -> AA, 28 -> AB, ...
#
# Example:
#   Input:  columnNumber = 28
#   Output: "AB"
#   Input:  columnNumber = 701
#   Output: "ZY"
#
# Constraints:
#   - 1 <= columnNumber <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# Similar to converting to base-26, but with a twist: there is no '0'
# (columns go A-Z, not 0-25). Subtract 1 before taking modulo to handle
# this 1-indexed nature. Repeatedly take (n-1) % 26 to get current char,
# then divide n by 26 (after adjusting).
#
# Time Complexity:  O(log n)  — number of digits in base-26
# Space Complexity: O(log n)  — result string
# ============================================================

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))

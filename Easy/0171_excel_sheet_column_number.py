# ============================================================
# LeetCode 171 - Excel Sheet Column Number
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a string columnTitle that represents the column title as appears
# in an Excel spreadsheet, return its corresponding column number.
#   A -> 1, B -> 2, ..., Z -> 26, AA -> 27, AB -> 28, ...
#
# Example:
#   Input:  columnTitle = "AB"
#   Output: 28
#   Input:  columnTitle = "ZY"
#   Output: 701
#
# Constraints:
#   - 1 <= columnTitle.length <= 7
#   - columnTitle consists only of uppercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Treat as base-26 conversion. Process left to right:
#   result = result * 26 + (char_value)
# where char_value = ord(char) - ord('A') + 1
#
# This is similar to converting a decimal string to int.
#
# Time Complexity:  O(n)  — n = length of columnTitle
# Space Complexity: O(1)
# ============================================================

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

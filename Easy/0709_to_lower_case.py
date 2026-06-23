# ============================================================
# LeetCode 709 - To Lower Case
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a string s, return the string after replacing every uppercase
# letter with the same lowercase letter.
#
# Example:
#   Input:  s = "Hello"    Output: "hello"
#   Input:  s = "LOVELY"   Output: "lovely"
#
# Constraints:
#   - 1 <= s.length <= 100
#   - s consists of printable ASCII characters.
#
# ============================================================
# THEORY / APPROACH:
# Python's built-in str.lower() handles all ASCII and Unicode cases.
# For a manual approach: for each char, if uppercase (ASCII 65-90),
# add 32 to convert to lowercase (ASCII 97-122). This uses the
# binary trick: set bit 5 (OR with 32) to lowercase an ASCII letter.
#
# Bit trick: 'A' | 32 = 'a', 'Z' | 32 = 'z'
# Useful insight for low-level string processing in robotics firmware.
#
# Time Complexity:  O(n)
# Space Complexity: O(n)  — output string
# ============================================================

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

    # Manual implementation using bit manipulation:
    # def toLowerCase(self, s: str) -> str:
    #     result = []
    #     for ch in s:
    #         if 'A' <= ch <= 'Z':
    #             result.append(chr(ord(ch) | 32))
    #         else:
    #             result.append(ch)
    #     return ''.join(result)

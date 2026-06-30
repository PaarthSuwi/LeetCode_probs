——# ============================================================
# LeetCode 1071 - Greatest Common Divisor of Strings
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# For two strings s and t, we say "t divides s" if and only if
# s = t + t + t + ... + t (t concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such
# that x divides both str1 and str2.
#
# Example 1:
#   Input:  str1 = "ABCABC", str2 = "ABC"
#   Output: "ABC"
#
# Example 2:
#   Input:  str1 = "ABABAB", str2 = "ABAB"
#   Output: "AB"
#
# Constraints:
#   - 1 <= str1.length, str2.length <= 1000
#   - str1 and str2 consist of uppercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Key insight: if a common divisor string x exists, then
# str1 + str2 == str2 + str1 must hold (order of concatenation
# does not matter when both are tiled by the same base string).
#
# If the above check passes, the answer length must be
# gcd(len(str1), len(str2)), mirroring the numeric GCD property.
# We return str1[:gcd(len(str1), len(str2))].
#
# Time Complexity: O(m + n) — single concatenation check
# Space Complexity: O(m + n) — temporary concatenated strings
# ============================================================

from math import gcd

class Solution:
      def gcdOfStrings(self, str1: str, str2: str) -> str:
                # A common divisor exists only if both concat orders match
                if str1 + str2 != str2 + str1:
                              return ""
                          # Length of GCD string == GCD of individual lengths
                          g = gcd(len(str1), len(str2))
                return str1[:g]

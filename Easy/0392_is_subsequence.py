# ============================================================
# LeetCode 392 - Is Subsequence
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given two strings s and t, return true if s is a subsequence of t,
# or false otherwise. A subsequence maintains relative order but
# doesn't need to be contiguous.
#
# Example:
#   Input:  s = "abc", t = "ahbgdc"   Output: True
#   Input:  s = "axc", t = "ahbgdc"   Output: False
#
# Constraints:
#   - 0 <= s.length <= 100
#   - 0 <= t.length <= 10^4
#   - s and t consist only of lowercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Two-pointer technique. One pointer i for s, one pointer j for t.
# Move j through t; whenever t[j] matches s[i], advance i.
# If i reaches len(s), all characters of s are matched.
#
# For follow-up (many queries against same t): preprocess t into a
# dict mapping char -> sorted list of positions, then use binary search.
#
# Time Complexity:  O(n)  — n = len(t)
# Space Complexity: O(1)
# ============================================================

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)

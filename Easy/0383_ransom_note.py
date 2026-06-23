# ============================================================
# LeetCode 383 - Ransom Note
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine. Each letter in
# magazine can only be used once.
#
# Example:
#   Input:  ransomNote = "aa", magazine = "aab"   Output: True
#   Input:  ransomNote = "aa", magazine = "ab"    Output: False
#
# Constraints:
#   - 1 <= ransomNote.length, magazine.length <= 10^5
#   - ransomNote and magazine consist of lowercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Count character frequencies in magazine using Counter (or dict).
# For each character in ransomNote, decrement its count in magazine.
# If any count goes below 0, the ransom note cannot be constructed.
#
# Time Complexity:  O(m + n)  — m = len(magazine), n = len(ransomNote)
# Space Complexity: O(1)      — at most 26 characters tracked
# ============================================================

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] <= 0:
                return False
            mag_count[ch] -= 1
        return True

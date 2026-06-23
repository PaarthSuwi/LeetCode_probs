# ============================================================
# LeetCode 290 - Word Pattern
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a pattern and a string s, find if s follows the same pattern.
# "Follow" means a full match such that there is a bijection between
# a letter in pattern and a non-empty word in s.
#
# Example:
#   Input:  pattern = "abba", s = "dog cat cat dog"   Output: True
#   Input:  pattern = "abba", s = "dog cat cat fish"  Output: False
#   Input:  pattern = "aaaa", s = "dog cat cat dog"   Output: False
#
# Constraints:
#   - 1 <= pattern.length <= 300
#   - pattern contains only lower-case English letters.
#   - 1 <= s.length <= 3000
#
# ============================================================
# THEORY / APPROACH:
# Bijection check using two hash maps: char->word and word->char.
# For each (char, word) pair, verify the mapping is consistent in both
# directions. A one-directional map would allow "abba" -> "dog dog dog dog".
#
# Time Complexity:  O(n)  — n = number of words
# Space Complexity: O(n)  — hash maps
# ============================================================

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                if word in word_to_char:
                    return False
                char_to_word[ch] = word
                word_to_char[word] = ch
        return True

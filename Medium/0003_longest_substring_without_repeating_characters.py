# ============================================================
# LeetCode 3 - Longest Substring Without Repeating Characters
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example 1:
#   Input:  s = "abcabcbb"
#   Output: 3   ("abc")
#
# Example 2:
#   Input:  s = "bbbbb"
#   Output: 1   ("b")
#
# Example 3:
#   Input:  s = "pwwkew"
#   Output: 3   ("wke")
#
# Constraints:
#   - 0 <= s.length <= 5 * 10^4
#   - s consists of English letters, digits, symbols and spaces.
#
# ============================================================
# THEORY / APPROACH:
# Sliding window with two pointers (left, right) and a hash map
# to store the most recent index of each character.
#
# Expand right pointer character by character.
# When a duplicate is found inside [left, right], move left past it.
# Track max window width throughout.
#
# Time Complexity: O(n) -- single pass with sliding window
# Space Complexity: O(min(m, n)) -- at most charset entries in hash map
# ============================================================

class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
                char_index = {}   # char -> last seen index
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
                      if ch in char_index and char_index[ch] >= left:
                                        left = char_index[ch] + 1
                                    char_index[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len

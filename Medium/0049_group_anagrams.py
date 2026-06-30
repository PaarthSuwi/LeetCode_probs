# ============================================================
# LeetCode 49 - Group Anagrams
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# Given an array of strings strs, group the anagrams together.
# An anagram is a word or phrase formed by rearranging the letters
# of another, using all the original letters exactly once.
# Return the answer in any order.
#
# Example 1:
#   Input:  strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#   Input:  strs = [""]
#   Output: [[""]]
#
# Constraints:
#   - 1 <= strs.length <= 10^4
#   - 0 <= strs[i].length <= 100
#   - strs[i] consists of lowercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Key insight: all anagrams have the same sorted form.
# Use a hash map: key = sorted(word), value = list of anagrams.
# Group all words by their sorted-character key and return the groups.
#
# Alternatively, use a 26-element character count tuple as the key
# for O(n * k) time instead of O(n * k log k).
#
# Time Complexity: O(n * k log k) -- sorting each word of length k
# Space Complexity: O(n * k) -- hash map storing all strings
# ============================================================

from collections import defaultdict
from typing import List

class Solution:
      def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                anagram_map = defaultdict(list)
                for s in strs:
                              key = tuple(sorted(s))  # canonical form
            anagram_map[key].append(s)
        return list(anagram_map.values())

# ============================================================
# LeetCode 1047 - Remove All Adjacent Duplicates In String
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal
# letters and removing them. Repeatedly make duplicate removals on s
# until we no longer can. Return the final string after all duplicate
# removals have been made.
#
# Example:
#   Input:  s = "abbaca"
#   Output: "ca"
#   Explanation: "abbaca" -> "aaca" -> "ca"
#
# Constraints:
#   - 1 <= s.length <= 10^5
#   - s consists of lowercase English letters.
#
# ============================================================
# THEORY / APPROACH:
# Use a stack. For each character in s:
#   - If the stack is non-empty and its top equals the current char,
#     pop the top (they cancel out as a duplicate pair).
#   - Otherwise, push the current char onto the stack.
# At the end, join the stack into a string.
#
# This simulates the repeated adjacent-duplicate removal in a single
# O(n) pass without actually looping multiple times.
#
# Time Complexity: O(n) — single pass through the string
# Space Complexity: O(n) — stack can hold up to n characters
# ============================================================

class Solution:
      def removeDuplicates(self, s: str) -> str:
                stack = []
                for ch in s:
                              if stack and stack[-1] == ch:
                                                stack.pop()
else:
                stack.append(ch)
          return "".join(stack)

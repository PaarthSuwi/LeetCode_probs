——# ============================================================
# LeetCode 1108 - Defanging an IP Address
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a valid (IPv4) IP address, return a defanged version of that
# IP address. A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
#   Input:  address = "1.1.1.1"
#   Output: "1[.]1[.]1[.]1"
#
# Example 2:
#   Input:  address = "255.100.50.0"
#   Output: "255[.]100[.]50[.]0"
#
# Constraints:
#   - The given address is a valid IPv4 address.
#
# ============================================================
# THEORY / APPROACH:
# Simple string replacement: replace every occurrence of "." with "[.]".
# Python's built-in str.replace() handles this in a single O(n) call.
#
# No edge cases to worry about since the input is guaranteed to be a
# valid IPv4 address (exactly three dots separating four octets).
#
# Time Complexity: O(n) — linear scan through the string
# Space Complexity: O(n) — output string proportional to input length
# ============================================================

class Solution:
      def defangIPaddr(self, address: str) -> str:
                return address.replace(".", "[.]")

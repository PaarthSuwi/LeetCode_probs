# ============================================================
# LeetCode 461 - Hamming Distance
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different. Given two integers x and y,
# return the Hamming distance between them.
#
# Example:
#   Input:  x = 1, y = 4
#   Output: 2
#   (1 = 0001, 4 = 0100 -> differ in 2 positions)
#
# Constraints:
#   - 0 <= x, y <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# XOR x and y: bits that differ become 1. Count the number of 1s
# in the XOR result using Brian Kernighan's algorithm or bin().count('1').
#
# Hamming distance is widely used in error correction codes, data
# compression, and is fundamental in information theory.
#
# Time Complexity:  O(1)  — at most 32 bits
# Space Complexity: O(1)
# ============================================================

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1  # Clear lowest set bit
            count += 1
        return count

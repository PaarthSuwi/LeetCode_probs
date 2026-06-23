# ============================================================
# LeetCode 191 - Number of 1 Bits (Hamming Weight)
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Write a function that takes the binary representation of a positive
# integer and returns the number of set bits (1s) it has.
# Also known as the Hamming weight.
#
# Example:
#   Input:  n = 11  (binary: 1011)
#   Output: 3
#   Input:  n = 128 (binary: 10000000)
#   Output: 1
#
# Constraints:
#   - 1 <= n <= 2^31 - 1
#
# ============================================================
# THEORY / APPROACH:
# Brian Kernighan's algorithm: n & (n-1) clears the lowest set bit.
# Count how many times we can do this until n becomes 0.
# This is faster than checking each bit when n is sparse.
#
# Relevance: Hamming weight is used in error detection, data compression,
# and bit flag counting in embedded/robotics systems.
#
# Time Complexity:  O(k)  — k = number of set bits
# Space Complexity: O(1)
# ============================================================

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # Clear lowest set bit
            count += 1
        return count

# ============================================================
# LeetCode 190 - Reverse Bits
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Reverse bits of a given 32-bit unsigned integer.
#
# Example:
#   Input:  n = 0b00000010100101000001111010011100 (43261596)
#   Output:    0b00111001011110000010100101000000 (964176192)
#
# Constraints:
#   - Input is a binary string of length 32
#
# ============================================================
# THEORY / APPROACH:
# Build the reversed number bit by bit. For each of 32 iterations:
#   1. Left shift result by 1 (make room for next bit)
#   2. OR the least significant bit of n into result
#   3. Right shift n by 1
#
# Relevant to robotics: bit manipulation is used in embedded systems,
# hardware register manipulation, FANUC/PLC bit masking operations.
#
# Time Complexity:  O(1)  — always 32 iterations
# Space Complexity: O(1)
# ============================================================

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

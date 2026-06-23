# ============================================================
# LeetCode 832 - Flipping an Image
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an n x n binary matrix image, flip the image horizontally,
# then invert it, and return the resulting image.
# Flip: reverse each row. Invert: 0 becomes 1 and 1 becomes 0.
#
# Example:
#   Input:  image = [[1,1,0],[1,0,1],[0,0,0]]
#   Output: [[1,0,0],[0,1,0],[1,1,1]]
#
# Constraints:
#   - n == image.length == image[i].length
#   - 1 <= n <= 20
#   - images[i][j] is either 0 or 1
#
# ============================================================
# THEORY / APPROACH:
# Two-pointer approach per row. Use left and right pointers.
# If left != right: swap and XOR each with 1 (flip + invert = just swap).
# If left == right (middle element in odd-length row): invert only.
# XOR trick: flipping then inverting = for equal elements: both change.
# For different elements: swap and they become equal (no net change needed).
#
# Time Complexity:  O(n^2)  — process each element
# Space Complexity: O(1)    — in-place modification
# ============================================================

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == row[right]:
                    row[left] ^= 1
                    row[right] ^= 1
                left += 1
                right -= 1
        return image

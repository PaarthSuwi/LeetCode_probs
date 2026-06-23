# ============================================================
# LeetCode 110 - Balanced Binary Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree: depth of the two subtrees of every
# node never differs by more than one.
#
# Example:
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: True
#   Input:  root = [1,2,2,3,3,null,null,4,4]
#   Output: False
#
# Constraints:
#   - Number of nodes in range [0, 5000]
#   - -10^4 <= Node.val <= 10^4
#
# ============================================================
# THEORY / APPROACH:
# DFS post-order: compute height of each subtree. If the absolute
# difference of left and right heights exceeds 1, or if any child
# returned -1 (unbalanced), return -1 to propagate the failure.
#
# Time Complexity:  O(n)  — each node visited once
# Space Complexity: O(h)  — recursion stack (h = tree height)
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1

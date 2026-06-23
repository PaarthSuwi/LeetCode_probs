# ============================================================
# LeetCode 101 - Symmetric Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a binary tree, check whether it is a mirror
# of itself (i.e., symmetric around its center).
#
# Example:
#   Input:  root = [1,2,2,3,4,4,3]
#   Output: True
#
#   Input:  root = [1,2,2,null,3,null,3]
#   Output: False
#
# Constraints:
#   - The number of nodes in the tree is in the range [1, 1000].
#   - -100 <= Node.val <= 100
#
# ============================================================
# THEORY / APPROACH:
# Use recursive DFS to compare the tree against its mirror.
# A tree is symmetric if its left subtree is a mirror of its
# right subtree. Two trees are mirrors if:
#   1. Their roots have the same value
#   2. Left's left subtree == Right's right subtree
#   3. Left's right subtree == Right's left subtree
#
# Time Complexity:  O(n)  — visit each node once
# Space Complexity: O(h)  — recursion stack depth h (height of tree)
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        return isMirror(root.left, root.right)

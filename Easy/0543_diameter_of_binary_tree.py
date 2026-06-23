# ============================================================
# LeetCode 543 - Diameter of Binary Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a binary tree, return the length of the diameter.
# The diameter is the length of the longest path between any two nodes.
# This path may or may not pass through the root.
# Length = number of edges in the path.
#
# Example:
#   Input:  root = [1,2,3,4,5]
#   Output: 3  (path: 4->2->1->3 or 5->2->1->3)
#
# Constraints:
#   - Number of nodes in range [1, 10^4]
#   - -100 <= Node.val <= 100
#
# ============================================================
# THEORY / APPROACH:
# DFS post-order. For each node, the diameter passing through it is
# left_height + right_height. Track the global maximum.
# Return the height (1 + max(left, right)) up to the parent.
#
# Key insight: diameter at a node = depth of left subtree + depth of right subtree.
#
# Time Complexity:  O(n)
# Space Complexity: O(h)  — recursion stack
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.max_diameter

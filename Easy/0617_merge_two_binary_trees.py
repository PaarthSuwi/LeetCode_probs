# ============================================================
# LeetCode 617 - Merge Two Binary Trees
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given two binary trees root1 and root2, merge them into a new tree.
# When two nodes overlap, sum their values. Otherwise use the existing node.
# Return the root of the merged tree.
#
# Example:
#   Input:  root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
#   Output: [3,4,5,5,4,null,7]
#
# Constraints:
#   - Number of nodes in both trees in range [0, 2000]
#   - -10^4 <= Node.val <= 10^4
#
# ============================================================
# THEORY / APPROACH:
# Simultaneous DFS on both trees. At each node:
# - If both exist: sum values, recurse on both children
# - If only one exists: return that node directly
# - If neither exists: return None
#
# Time Complexity:  O(min(m, n))  — m, n = nodes in each tree
# Space Complexity: O(min(m, n))  — recursion stack
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

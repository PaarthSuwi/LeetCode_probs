# ============================================================
# LeetCode 112 - Path Sum
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a binary tree and an integer targetSum, return true
# if the tree has a root-to-leaf path such that adding all values along
# the path equals targetSum. A leaf is a node with no children.
#
# Example:
#   Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: True  (path: 5 -> 4 -> 11 -> 2)
#   Input:  root = [1,2,3], targetSum = 5
#   Output: False
#
# Constraints:
#   - Number of nodes in range [0, 5000]
#   - -1000 <= Node.val <= 1000
#   - -1000 <= targetSum <= 1000
#
# ============================================================
# THEORY / APPROACH:
# Recursive DFS. At each node, subtract its value from the target.
# At a leaf node, check if the remaining target equals the leaf's value.
# Short-circuit: return True as soon as any valid path is found.
#
# Time Complexity:  O(n)  — visit each node once in worst case
# Space Complexity: O(h)  — recursion stack (h = height of tree)
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))

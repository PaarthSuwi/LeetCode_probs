# ============================================================
# LeetCode 653 - Two Sum IV - Input is a BST
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a BST and an integer k, return true if there exist
# two elements in the BST such that their sum is equal to k.
#
# Example:
#   Input:  root = [5,3,6,2,4,null,7], k = 9
#   Output: True  (3 + 6 = 9)
#   Input:  root = [5,3,6,2,4,null,7], k = 28
#   Output: False
#
# Constraints:
#   - Number of nodes in range [1, 10^4]
#   - -10^4 <= Node.val <= 10^4
#   - Root is a valid BST
#   - -10^5 <= k <= 10^5
#
# ============================================================
# THEORY / APPROACH:
# DFS traversal + hash set. For each node with value v, check if
# (k - v) exists in the seen set. Add v to the set and continue.
# This is a classic two-sum pattern adapted for trees.
#
# Time Complexity:  O(n)
# Space Complexity: O(n)  — hash set
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

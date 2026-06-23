# ============================================================
# LeetCode 700 - Search in a Binary Search Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are given the root of a BST and an integer val. Find the node
# in the BST where the node's value equals val and return the subtree
# rooted at that node. If no such node exists, return null.
#
# Example:
#   Input:  root = [4,2,7,1,3], val = 2
#   Output: [2,1,3]
#
# Constraints:
#   - Number of nodes in range [1, 5000]
#   - 1 <= Node.val <= 10^7
#   - Root is a valid BST
#   - 1 <= val <= 10^7
#
# ============================================================
# THEORY / APPROACH:
# Exploit BST property: if val < node.val, go left; if val > node.val,
# go right; if equal, return node. Iterative approach avoids recursion overhead.
#
# Direct application of BST lookup — fundamental for robotics state-space
# lookup tables and configuration databases.
#
# Time Complexity:  O(h)  — h = height (O(log n) balanced)
# Space Complexity: O(1)  — iterative
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if val == node.val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None

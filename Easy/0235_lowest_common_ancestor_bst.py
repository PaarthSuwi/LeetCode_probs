# ============================================================
# LeetCode 235 - Lowest Common Ancestor of a BST
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a BST, find the lowest common ancestor (LCA) of two given nodes p and q.
# LCA is the lowest node that has both p and q as descendants (a node is a
# descendant of itself).
#
# Example:
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2
#
# Constraints:
#   - Number of nodes in range [2, 10^5]
#   - -10^9 <= Node.val <= 10^9
#   - All Node.val are unique.
#
# ============================================================
# THEORY / APPROACH:
# Exploit BST property: if both p and q are smaller than root, LCA is in
# left subtree. If both are larger, LCA is in right subtree. Otherwise,
# root itself is the LCA (split point).
#
# Time Complexity:  O(h)  — h = height of BST (O(log n) balanced)
# Space Complexity: O(1)  — iterative, no recursion stack
# ============================================================

class TreeNode:
    def __init__(self, x):
        self.val = x; self.left = None; self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

# ============================================================
# LeetCode 145 - Binary Tree Postorder Traversal
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a binary tree, return the postorder traversal
# of its nodes' values. Postorder: Left -> Right -> Root.
#
# Example:
#   Input:  root = [1,null,2,3]
#   Output: [3,2,1]
#
# Constraints:
#   - Number of nodes in range [0, 100]
#   - -100 <= Node.val <= 100
#
# ============================================================
# THEORY / APPROACH:
# Iterative approach: use a stack, but push root, right, left and
# collect results in reverse (or use a modified preorder and reverse).
# Process: root -> right -> left, then reverse result gives left -> right -> root.
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

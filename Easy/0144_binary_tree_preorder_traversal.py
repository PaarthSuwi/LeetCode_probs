# ============================================================
# LeetCode 144 - Binary Tree Preorder Traversal
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the root of a binary tree, return the preorder traversal
# of its nodes' values. Preorder: Root -> Left -> Right.
#
# Example:
#   Input:  root = [1,null,2,3]
#   Output: [1,2,3]
#
# Constraints:
#   - Number of nodes in range [0, 100]
#   - -100 <= Node.val <= 100
#
# ============================================================
# THEORY / APPROACH:
# Iterative approach using a stack. Push root, then repeatedly pop and
# visit node, push right child first (then left), so left is processed next.
# Preorder: visit node BEFORE its children.
#
# Recursive alternative also shown (simpler but uses implicit call stack).
#
# Time Complexity:  O(n)  — visit every node once
# Space Complexity: O(n)  — stack can hold up to n nodes
# ============================================================

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# ============================================================
# LeetCode 111 - Minimum Depth of Binary Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given a binary tree, find its minimum depth. The minimum depth is
# the number of nodes along the shortest path from root to the nearest
# leaf node. Note: a leaf is a node with no children.
#
# Example:
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: 2
#   Input:  root = [2,null,3,null,4,null,5,null,6]
#   Output: 5
#
# Constraints:
#   - Number of nodes in range [0, 10^5]
#   - -1000 <= Node.val <= 1000
#
# ============================================================
# THEORY / APPROACH:
# BFS level-order traversal. The first leaf node we encounter is the
# shallowest one. BFS explores nodes level by level, so the first leaf
# gives the minimum depth without needing to explore the full tree.
#
# Time Complexity:  O(n)  — at most all nodes visited
# Space Complexity: O(w)  — w = max width of tree (BFS queue size)
# ============================================================

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0

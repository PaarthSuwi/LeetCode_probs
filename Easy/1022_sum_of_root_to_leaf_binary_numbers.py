# ============================================================
# LeetCode 1022 - Sum of Root To Leaf Binary Numbers
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are given the root of a binary tree where each node has a value of 0 or 1.
# Each root-to-leaf path represents a binary number. Return the sum of these numbers.
#
# Example:
#   Input:  root = [1,0,1,0,1,0,1]
#   Output: 22  (binary: 100 + 101 + 110 + 111 = 4+5+6+7 = 22)
#
# Constraints:
#   - Number of nodes in range [1, 1000]
#   - Node.val is 0 or 1.
#
# ============================================================
# THEORY / APPROACH:
# DFS with current accumulated value. At each node, shift the current
# value left by 1 (multiply by 2) and add node.val. At a leaf node,
# add the accumulated value to the total.
#
# Bit-shifting to build binary numbers is core to embedded/robotics
# firmware development (parsing sensor data packets, CAN bus frames, etc.)
#
# Time Complexity:  O(n)
# Space Complexity: O(h)  — recursion stack
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            current = (current << 1) | node.val
            if not node.left and not node.right:
                return current
            return dfs(node.left, current) + dfs(node.right, current)
        return dfs(root, 0)

# ============================================================
# LeetCode 108 - Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given an integer array nums where the elements are sorted in
# ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is one where the depth of the two
# subtrees of every node never differs by more than one.
#
# Example:
#   Input:  nums = [-10,-3,0,5,9]
#   Output: [0,-3,9,-10,null,5]
#
# Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4
#   - nums is sorted in strictly increasing order.
#
# ============================================================
# THEORY / APPROACH:
# Recursively pick the middle element as the root. This balances the
# tree because equal (or near-equal) numbers of elements go left and right.
# Apply the same logic recursively to left half and right half.
#
# Time Complexity:  O(n)      — every element becomes a node
# Space Complexity: O(log n)  — recursion stack depth (balanced tree height)
# ============================================================

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

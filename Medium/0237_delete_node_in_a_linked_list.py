# ============================================================
# LeetCode 237 - Delete Node in a Linked List
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# There is a singly-linked list and you are given a node to delete.
# You are NOT given access to the head of the list. The node to delete
# is guaranteed to NOT be the tail. Delete the given node.
#
# Example:
#   Input:  head = [4,5,1,9], node = 5
#   Output: [4,1,9]
#
# Constraints:
#   - Number of nodes in range [2, 1000]
#   - -1000 <= Node.val <= 1000
#   - The node to be deleted is not the tail.
#   - All node values are unique.
#
# ============================================================
# THEORY / APPROACH:
# Since we cannot access the previous node, we CANNOT unlink node normally.
# Instead: copy the next node's value into current node, then unlink the next node.
# Effectively we "replace" the current node with the next node's data.
#
# node.val = node.next.val
# node.next = node.next.next
#
# This is an unconventional trick — we destroy the next node, not the target.
#
# Time Complexity:  O(1)
# Space Complexity: O(1)
# ============================================================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# ============================================================
# LeetCode 141 - Linked List Cycle
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given head, the head of a linked list, determine if the linked list
# has a cycle. A cycle exists if some node can be reached again by
# continuously following the next pointer.
#
# Example:
#   Input:  head = [3,2,0,-4], pos = 1 (tail connects to index 1)
#   Output: True
#   Input:  head = [1,2], pos = -1
#   Output: False
#
# Constraints:
#   - Number of nodes in range [0, 10^4]
#   - -10^5 <= Node.val <= 10^5
#   - pos is -1 or a valid index in the linked list
#
# ============================================================
# THEORY / APPROACH:
# Floyd's Cycle Detection (Tortoise and Hare algorithm).
# Two pointers: slow (1 step) and fast (2 steps).
# If there is a cycle, fast will eventually lap slow and they meet.
# If no cycle, fast reaches None first.
# This avoids using a hash set (O(1) space vs O(n) space).
#
# Time Complexity:  O(n)  — at most 2 passes through the list
# Space Complexity: O(1)  — only two pointers
# ============================================================

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

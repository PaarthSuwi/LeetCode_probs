# ============================================================
# LeetCode 160 - Intersection of Two Linked Lists
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the heads of two singly linked lists headA and headB, return the
# node at which they intersect. If they do not intersect, return null.
# The intersection is by reference (same node object), not by value.
#
# Example:
#   Input:  listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA=2, skipB=3
#   Output: Intersected at node with val = 8
#
# Constraints:
#   - Number of nodes in listA: [1, 3*10^4]
#   - Number of nodes in listB: [1, 3*10^4]
#   - -10^5 <= Node.val <= 10^5
#
# ============================================================
# THEORY / APPROACH:
# Two-pointer technique. Both pointers start at their respective heads.
# When one pointer reaches the end, redirect it to the other list's head.
# After at most one swap each, both pointers traverse the same total length
# (lenA + lenB) and will meet at the intersection or both reach None.
#
# Time Complexity:  O(m + n)  — each pointer traverses both lists
# Space Complexity: O(1)
# ============================================================

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

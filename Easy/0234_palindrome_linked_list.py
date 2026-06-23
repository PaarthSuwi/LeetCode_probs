# ============================================================
# LeetCode 234 - Palindrome Linked List
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Given the head of a singly linked list, return true if it is a palindrome
# or false otherwise.
#
# Example:
#   Input:  head = [1,2,2,1]   Output: True
#   Input:  head = [1,2]       Output: False
#
# Constraints:
#   - Number of nodes in range [1, 10^5]
#   - 0 <= Node.val <= 9
#
# ============================================================
# THEORY / APPROACH:
# 1. Find the middle using slow/fast pointers.
# 2. Reverse the second half of the list in-place.
# 3. Compare first half with reversed second half.
# 4. (Optional) Restore the list.
#
# This achieves O(n) time and O(1) space by avoiding copying to an array.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

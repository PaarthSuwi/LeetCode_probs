# ============================================================
# LeetCode 21 - Merge Two Sorted Lists
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made
# by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#
# Example:
#   Input:  list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
#
# Constraints:
#   - The number of nodes in both lists is in the range [0, 50].
#   - -100 <= Node.val <= 100
#   - Both list1 and list2 are sorted in non-decreasing order.
#
# ============================================================
# THEORY / APPROACH:
# Use a dummy head node and two pointers to iterate through both lists.
# Compare the current nodes of both lists; append the smaller one to
# the result and advance that pointer. When one list is exhausted,
# append the remaining tail of the other list.
#
# Time Complexity:  O(m + n)  — traverse both lists once
# Space Complexity: O(1)      — only pointer manipulation, no extra nodes
# ============================================================

from typing import Optional

class ListNode:
      def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

  class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                  dummy = ListNode(0)
                  current = dummy

            while list1 and list2:
                          if list1.val <= list2.val:
                                            current.next = list1
                                            list1 = list1.next
else:
                current.next = list2
                  list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

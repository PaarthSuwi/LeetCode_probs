# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left
# of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge, left sum is 0 (no elements to the left).
# Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)  # compute total sum once
        left_sum = 0

        for i, val in enumerate(nums):
            # right sum = total - left_sum - current element
            if left_sum == total - left_sum - val:
                return i   # found leftmost pivot
            left_sum += val  # expand left window

        return -1  # no pivot found

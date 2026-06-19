// 724. Find Pivot Index

// Given an array of integers nums, calculate the pivot index of this array.

// The pivot index is the index where the sum of all the numbers strictly to the left
// of the index is equal to the sum of all the numbers strictly to the index's right.

// If the index is on the left edge of the array, then the left sum is 0 because there
// are no elements to the left. Return the leftmost pivot index. If no such index exists, return -1.

#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        for (int x : nums) total += x; // compute total sum once

        int leftSum = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            // right sum = total - leftSum - nums[i]
            if (leftSum == total - leftSum - nums[i]) {
                return i; // found the pivot index
            }
            leftSum += nums[i]; // expand left window
        }

        return -1; // no pivot found
    }
};

# ============================================================
# LeetCode 1732 - Find the Highest Altitude
# Difficulty: Medium
# ============================================================
#
# QUESTION:
# A biker is going on a road trip. The trip consists of n + 1 points at
# different altitudes. The biker starts at altitude 0. You are given an
# integer array gain of length n where gain[i] is the net altitude change
# between point i and point i + 1. Return the highest altitude of a point.
#
# Example:
#   Input:  gain = [-5,1,5,0,-7]
#   Output: 1  (altitudes: [0,-5,-4,1,1,-6], max = 1)
#
# Constraints:
#   - n == gain.length
#   - 1 <= n <= 100
#   - -100 <= gain[i] <= 100
#
# ============================================================
# THEORY / APPROACH:
# Prefix sum: maintain running altitude. Start at 0, accumulate gains.
# Track maximum altitude seen.
#
# This is directly applicable to robotics: tracking robot elevation from
# IMU/barometer differential readings, or odometry position tracking.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current = 0
        for g in gain:
            current += g
            max_alt = max(max_alt, current)
        return max_alt

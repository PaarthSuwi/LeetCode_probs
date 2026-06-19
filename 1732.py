# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between
# points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution(object):
    def largestAltitude(self, gain):
        max_alt = 0     # starting altitude is 0, so our answer is at least 0
        current = 0     # current altitude tracker

        for g in gain:
            current += g                    # accumulate gain step by step
            max_alt = max(max_alt, current) # track the peak

        return max_alt

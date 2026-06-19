// 1732. Find the Highest Altitude

// There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
// The biker starts his trip on point 0 with altitude equal 0.

// You are given an integer array gain of length n where gain[i] is the net gain in altitude between
// points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maxAlt = 0;       // starting altitude is 0, so answer is at least 0
        int current = 0;      // track current altitude as we traverse

        for (int i = 0; i < (int)gain.size(); ++i) {
            current += gain[i];            // update altitude at each step
            maxAlt = max(maxAlt, current); // keep track of the highest seen
        }

        return maxAlt;
    }
};

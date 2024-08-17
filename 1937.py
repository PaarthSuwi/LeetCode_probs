# 1937. Maximum number of points with cost 

# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

#     x for x >= 0.
#     -x for x < 0.

class Solution(object):
    def maxPoints(self, points):

        m, n = len(points), len(points[0])
    
        dp = points[0]
        
        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            left_max[0] = dp[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c-1] - 1, dp[c])

            right_max[n-1] = dp[n-1]
            for c in range(n-2, -1, -1):
                right_max[c] = max(right_max[c+1] - 1, dp[c])
            
            for c in range(n):
                dp[c] = points[r][c] + max(left_max[c], right_max[c])
        
        return max(dp)

        """
        :type points: List[List[int]]
        :rtype: int
        """
        

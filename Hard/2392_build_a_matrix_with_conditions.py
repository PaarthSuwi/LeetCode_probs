# ============================================================
# LeetCode 2392 - Build a Matrix With Conditions
# Difficulty: Hard
# ============================================================
#
# QUESTION:
# You are given a k x k matrix of zeros and two lists of conditions:
# rowConditions and colConditions. Each condition [u, v] means u must
# appear in a row above v. Place integers 1..k so each appears exactly once,
# satisfying all row and column conditions. Return the matrix, or empty if impossible.
#
# Example:
#   Input:  k=3, rowConditions=[[1,2],[3,2]], colConditions=[[2,1],[3,2]]
#   Output: [[3,0,0],[0,0,1],[0,2,0]]
#
# Constraints:
#   - 2 <= k <= 400
#   - 1 <= rowConditions.length, colConditions.length <= 10^4
#   - rowConditions[i].length == colConditions[i].length == 2
#   - 1 <= abi, abi <= k
#
# ============================================================
# THEORY / APPROACH:
# Topological sort (Kahn's algorithm / BFS) on both row and column conditions.
# 1. Build a directed graph from conditions: u -> v means u comes before v.
# 2. Run topo sort to get row ordering and column ordering.
# 3. If a cycle exists (not all nodes ordered), return [].
# 4. Build the matrix: for each number, place it at (row_pos[num], col_pos[num]).
#
# Topological sort is fundamental in task scheduling, dependency resolution,
# and robot motion sequencing (ordering motion primitives with dependencies).
#
# Time Complexity:  O(k + n)  — n = number of conditions
# Space Complexity: O(k + n)  — adjacency list and degree arrays
# ============================================================

from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions):
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            queue = deque([i for i in range(1, k+1) if in_degree[i] == 0])
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for nxt in graph[node]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        return matrix

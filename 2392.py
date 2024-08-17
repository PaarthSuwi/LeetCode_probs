#  2392. Build a Matrix With Conditions

#  You are given a positive integer k. You are also given:

#    a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
#     a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].

# The two arrays contain integers from 1 to k.

# You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

#  The matrix should also satisfy the following conditions:

#     The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
#     The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.

# Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.


from collections import defaultdict, deque

def topological_sort(conditions, k):
    graph = defaultdict(list)
    indegree = [0] * k
    
    for u, v in conditions:
        graph[u-1].append(v-1)
        indegree[v-1] += 1
    
    queue = deque([i for i in range(k) if indegree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return order if len(order) == k else []

def buildMatrix(k, rowConditions, colConditions):
    rowOrder = topological_sort(rowConditions, k)
    colOrder = topological_sort(colConditions, k)
    
    if not rowOrder or not colOrder:
        return []
    
    matrix = [[0] * k for _ in range(k)]
    pos = {num: (i, j) for i, num in enumerate(rowOrder) for j, col in enumerate(colOrder) if col == num}
    
    for num, (r, c) in pos.items():
        matrix[r][c] = num + 1
    
    return matrix


 
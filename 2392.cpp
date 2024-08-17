//  2392. Build a Matrix With Conditions

//  You are given a positive integer k. You are also given:

//    a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
//     a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].

// The two arrays contain integers from 1 to k.

// You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

//  The matrix should also satisfy the following conditions:

//      The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
//      The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.

//  Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

#include <iostream>
#include <vector>
#include <queue>
#include <cstring> // for memset
using namespace std;

class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        int rowOrder[k], colOrder[k];  // Use arrays instead of vectors for orders
        if (!topologicalSort(k, rowConditions, rowOrder) || !topologicalSort(k, colConditions, colOrder)) {
            return {}; // Return empty matrix if topological sort fails
        }
        
        vector<vector<int>> matrix(k, vector<int>(k, 0)); // Matrix of size k x k initialized to 0
        
        int rowPos[k], colPos[k];
        
        for (int i = 0; i < k; ++i) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }
        
        for (int i = 0; i < k; ++i) {
            matrix[rowPos[i]][colPos[i]] = i + 1;
        }
        
        return matrix;
    }

private:
    bool topologicalSort(int k, const vector<vector<int>>& conditions, int* order) {
        int indegree[k];
        memset(indegree, 0, sizeof(indegree)); // Initialize indegree array to 0
        
        vector<int> graph[k];
        
        for (const auto& cond : conditions) {
            graph[cond[0] - 1].push_back(cond[1] - 1);
            indegree[cond[1] - 1]++;
        }
        
        queue<int> q;
        int idx = 0;
        
        for (int i = 0; i < k; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            order[idx++] = node;
            
            for (int neighbor : graph[node]) {
                if (--indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        return idx == k; // Return true if all nodes are sorted
    }
};

class Solution:
    def __init__(self):
        self.result = []
        self.path = [0]
    
    def allPathsSourceTarget(self, graph):
        if not graph:
            return []
        self.dfs(graph, 0)
        return self.result
    
    def dfs(self, graph, root: int):
        if root == len(graph) - 1:
            #Deep copy must be used for a list in backtracking
            self.result.append(self.path[:])
            return
        
        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop() #backtracking


if __name__ == '__main__':
    #Test data
    graph_1 = [[1,2],[3],[3],[]]
    graph_2 = [[4,3,1],[3,2,4],[3],[4],[]]
    
    print(Solution().allPathsSourceTarget(graph_1))
    print(Solution().allPathsSourceTarget(graph_2))
class Solution:   
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
print(s.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
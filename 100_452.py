class Solution:   
    def findMinArrowShots(self, points):
        if len(points) == 0:
            return 0
        points.sort(key = lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
        return result

s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(s.findMinArrowShots([[1,2]]))
print(s.findMinArrowShots([[2,3],[2,3]]))
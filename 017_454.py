class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        record = {}
        for n1 in nums1:
            for n2 in nums2:
                record[n1+n2] = record.get(n1+n2, 0) + 1
                
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -(n3 + n4)
                if key in record:
                    count += record[key]
        return count

s = Solution()
print(s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
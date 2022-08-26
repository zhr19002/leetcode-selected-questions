class Solution:
    def fourSum(self, nums, target):
        record = {}
        for i in nums:
            record[i] = record.get(i, 0) + 1
        
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in record:
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if record[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

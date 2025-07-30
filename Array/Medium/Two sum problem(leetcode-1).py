class Solution:
    def twosum(self, nums, target):
        hashmap = {}  # To store value:index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i
nums=[1,2,3,4,5]
target=7
obj=Solution()
print(obj.twosum(nums,target))
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such element found, find the next bigger element from the right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the sub-array after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
nums = [3,2,1]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]

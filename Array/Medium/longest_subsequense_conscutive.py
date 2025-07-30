class Solution:
    def longest_subsequense_consecutive(self, array):
        nums = set(array)
        length = 0
        
        for i in nums:
            if i - 1 not in nums:
                count = 1
                current = i
                
                while current+ 1 in nums:
                    count += 1
                    current+= 1
                
                length = max(length, count)  # <-- Move this inside the 'if' block
                
        return length

# Test case
array = [100,101,102,3,4]
obj = Solution()
print(obj.longest_subsequense_consecutive(array))  # Output: 5

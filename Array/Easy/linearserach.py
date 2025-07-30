class Solution:
    def linear_search(self, array, key):
        for i in range(len(array)):
            if array[i] == key:
                return i  # Element found at index i
        return -1  # Element not found

# Example
array = [10, 20, 30, 40, 50]
key = 30

obj = Solution()
index = obj.linear_search(array, key)
print("Element found at index:", index if index != -1 else "Not found")

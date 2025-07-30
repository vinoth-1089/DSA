class Solution:
    def union_array(self, array_a, array_b):
        i = j = 0
        n, m = len(array_a), len(array_b)
        result = []

        while i < n and j < m:
            if array_a[i] < array_b[j]:
                if not result or result[-1] != array_a[i]:       
                    result.append(array_a[i])
                i += 1
            elif array_b[j] < array_a[i]:
                if not result or result[-1] != array_b[j]:
                    result.append(array_b[j])
                j += 1
            else:
                if not result or result[-1] != array_a[i]:
                    result.append(array_a[i])
                i += 1
                j += 1

        # Append remaining elements
        while i < n:
            if not result or result[-1] != array_a[i]:
                result.append(array_a[i])
            i += 1

        while j < m:
            if not result or result[-1] != array_b[j]:
                result.append(array_b[j])
            j += 1  

        return result

# Example usage
array_a = [1, 2, 3, 4, 5]
array_b = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
print(obj.union_array(array_a, array_b))

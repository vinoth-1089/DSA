class Solution:
    def rearrange_by_sign(self, array):
        pos = []
        neg = []

        for num in array:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []
        i = j = 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        # Append remaining elements
        result.extend(pos[i:])
        result.extend(neg[j:])
 
        return result


array = [1, 2, 6, 7, -4, -5]
obj = Solution()
print(obj.rearrange_by_sign(array))
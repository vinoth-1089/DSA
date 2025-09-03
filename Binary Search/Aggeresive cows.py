class Solution:
    
    def find_min_distance_bte_cows(self, array, cows):
        array.sort() 
        low = 0
        high = array[-1] - array[0]
        ans = 0

        def possible(array, mid, cows):
            count_of_cows = 1
            last_cow = array[0]

            for i in range(1, len(array)):
                if array[i] - last_cow >= mid:
                    count_of_cows += 1
                    last_cow = array[i]
                if count_of_cows >= cows:
                    return True
            return False

 
        while low <= high:
            mid = (low + high) // 2
            if possible(array, mid, cows):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
s = Solution()
print(s.find_min_distance_bte_cows([1,2,8,4,9], 3))  


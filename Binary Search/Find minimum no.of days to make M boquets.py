<<<<<<< HEAD
class Solution:

    def find_mini_day_to_make_Boquets(self, array, M, K):
        low = min(array)
        high = max(array)
        ans = -1

        if M * K > len(array):
            return -1

        while low <= high:
            mid = (low + high) // 2

            if self.can_make_boquets(array, mid, K, M):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def can_make_boquets(self, array, day, K, M):
        count = 0
        bouquets = 0

        for bloom in array:
            if bloom <= day:
                count += 1
                if count == K:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= M

# Example usage
bloomday = [1, 10, 3, 10, 2]
m = int(input("\nEnter number of Bouquets: "))
k = int(input("Enter number of flowers per Bouquet: "))

obj = Solution()
result = obj.find_mini_day_to_make_Boquets(bloomday, m, k)
print("\nMinimum number of days required:", result)
=======
class Solution:

    def find_mini_day_to_make_Boquets(self, array, M, K):
        low = min(array)
        high = max(array)
        ans = -1

        if M * K > len(array):
            return -1

        while low <= high:
            mid = (low + high) // 2

            if self.can_make_boquets(array, mid, K, M):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def can_make_boquets(self, array, day, K, M):
        count = 0
        bouquets = 0

        for bloom in array:
            if bloom <= day:
                count += 1
                if count == K:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= M

# Example usage
bloomday = [1, 10, 3, 10, 2]
m = int(input("\nEnter number of Bouquets: "))
k = int(input("Enter number of flowers per Bouquet: "))

obj = Solution()
result = obj.find_mini_day_to_make_Boquets(bloomday, m, k)
print("\nMinimum number of days required:", result)
>>>>>>> daf84cd7edad7e66253a7542968eef25d52d94cf

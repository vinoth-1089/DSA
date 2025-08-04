class solution():
    
    def find_the_sqrt_number(self,n):
        
        low=1
        high=n
        ans=1
        
        while (low<=high):
            mid=(low+high)//2
            
            squre=mid*mid
            if squre==n:
                return mid
            elif squre<n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
n=int(input("\n Enter the Number:"))
obj=solution()
sqrt=obj.find_the_sqrt_number(n)
print(f"\n The Square root of {n} is",sqrt)
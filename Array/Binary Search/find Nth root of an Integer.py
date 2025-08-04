class solution():
    
    
    def find_n_root_Intger(self,n,m):
        
        low=1
        high=m
       
        
        while(low<=high):
            
            mid = (low+high)//2
            
            ans=self.root(n,mid)
            
            if m==ans:
                return mid
            elif m<ans:
                high=mid-1
            else:
                low=mid+1
        return -1
    def root(self,n,mid):
        sqrt=1
        for _ in range(n):
           sqrt*=mid
        return sqrt
n=int(input("\n Enter a number:"))
m=int(input("\n Enter a number:"))
obj=solution()
result=obj.find_n_root_Intger(n,m)
print(result)

import math

class solution:
    
    def Find_mini_divisor_thershold(self,array,thersold):
        
        low=1
        high=max(array)
        result=0
        while(low<=high):
            
            mid=(low+high)//2
            
            if self.Mini_Divisor(array,mid,thersold):
                result=mid
                high=mid-1
            else:
               low=mid+1       
        return result
    
    def Mini_Divisor(self,array,divisor,thersold):
        
        total=0
        for i in array:
            
            total+=math.ceil(i/divisor)
            
        return total <= thersold
    
    
array=[1, 2, 6, 8, 5, 4]    
thersold=8
obj=solution()
result=obj.Find_mini_divisor_thershold(array,thersold)
print(result)
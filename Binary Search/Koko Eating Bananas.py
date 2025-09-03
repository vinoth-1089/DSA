<<<<<<< HEAD
import math
class solution:
    
    
    def Find_Koko_Eating_Banans(self,array,hour):
        
        low=1
        high=max(array)
        result=high
        while(low<=high):
            
            mid=(low+high)//2
            total_time=self.time(array,mid)
            
            if total_time <=hour:
                result=mid
                high=mid-1
           
            else:
                low=mid+1
        return result
    def time(self,array,hour):
        ans=0
        for i in array:
            ans+=math.ceil(i/hour)
        return ans
array=[3,6,7,11]
hour=8
obj=solution()
result=obj.Find_Koko_Eating_Banans(array,hour)
print(result)
            
                                
            
=======
import math
class solution:
    
    
    def Find_Koko_Eating_Banans(self,array,hour):
        
        low=1
        high=max(array)
        result=high
        while(low<=high):
            
            mid=(low+high)//2
            total_time=self.time(array,mid)
            
            if total_time <=hour:
                result=mid
                high=mid-1
           
            else:
                low=mid+1
        return result
    def time(self,array,hour):
        ans=0
        for i in array:
            ans+=math.ceil(i/hour)
        return ans
array=[3,6,7,11]
hour=8
obj=solution()
result=obj.Find_Koko_Eating_Banans(array,hour)
print(result)
            
                                
            
>>>>>>> daf84cd7edad7e66253a7542968eef25d52d94cf
            
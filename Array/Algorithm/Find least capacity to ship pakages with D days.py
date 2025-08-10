class solution:
    
    def find_least_capacity_to_ship_D_days(self,array,day):
        
        low=max(array)
        high=sum(array)
        ans=-1
        while(low<=high):
            
            mid=(low+high)//2
            reqdays=self.possible(array,mid)
            if reqdays<= day:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def possible(self,array,mid):
        
    
        days=1
        load=0
        for i in array:
            if load+i > mid:
                days+=1
                load=i
            else:
                load+=i
                
            
        return days
array=[5,10,2,7,16]
day=3
obj=solution()
result=obj.find_least_capacity_to_ship_D_days(array,day)
print(result)
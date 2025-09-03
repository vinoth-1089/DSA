class solution:
    
    def find_kth_missing_number(Self,array,k):
        
        low=0
        high=len(array)-1
        
        while(low<=high):
            
            mid=(low+high)//2
            missing =array[mid]- (mid+1)
            if(missing) <k:
                low=mid+1
               
            else:
              high=mid-1  
        return low+k
array=[2,3,4,7,11]
k=5
obj=solution()
result=obj.find_kth_missing_number(array,k)  
print(result)             
    
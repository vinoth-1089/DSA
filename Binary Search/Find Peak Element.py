class solution:
    
    def find_peak_element(self,array):
        
        n=len(array)
        
        if(n==1):return array[0]
        if (array[0]>array[1]):return array[0]
        
        if (array[n-1]>array[n-2]):return array[n-1]
        
        low = 1
        high = n-2
        
        while(low<=high):
            
            mid = (low+high)//2
            
            if(array[mid-1]<array[mid]>array[mid+1]):  return mid # to check the element is mid 
            
            if(array[mid]>array[mid-1]): # check whether peak element is left side or in right side
                low=mid+1                # if the  array[mid] is 5 and  array[mid] is 4 in this 
            else:
                high=mid-1               # case 5>4 so the peak element in right side so low pointer will be changing and
                                         # else part is vice versa
         
array=[1,2,3,4,5,6,7,8,5,2]
obj=solution()
result=obj.find_peak_element(array)
print(" The Peak Element of Array is "+str(array[result])+"\t And the index is ",result)

class solution:
    
    #using dutch national flag algorithm
    def sort_012(self,array):
        
        low=0
        mid=0
        high=len(array)-1
         
        while mid<=high:
            
            if array[mid]==0:
                array[low],array[mid]=array[mid],array[low]
                low+=1
                mid+=1

            elif array[mid]==1:
                mid+=1
                
            else:
                array[mid],array[high]=array[high],array[mid]
                high-=1
        return array
array=[2,0,2,1,1,0,2]
obj=solution()
print(obj.sort_012(array))
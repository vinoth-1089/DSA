class  solution:
    
    
    def mini_element_sorted_rotate_array(self,array):
        low=0
        high=len(array)-1
        min_ele = float('inf')

        
        while low<=high:
            
            mid=(low+high)//2
            
            if array[low]<=array[high]:
                min_ele=array[low]
                break
            
            if  array[low]<=array[mid]:
                min_ele=array[low]
                low=mid+1
            else:
                min_ele=min(min_ele,array[mid])
                high=mid-1
        return min_ele
array=[7,8,9,1,2,3,4,5,6]
obj=solution()
print(obj.mini_element_sorted_rotate_array(array))
            
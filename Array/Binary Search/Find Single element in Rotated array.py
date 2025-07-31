class solution:
    
    def find_single_Element(self,array):
        
        n=len(array)
        
        left=1
        right=n-2
        
        if n==1:
            return array[0]
        
        if array[left]!=array[left-1]: return array[left]
        
        if array[n-1]!=array[n-2]: return array[n-2]
        
        while(left<=right):
            
            mid = (left+right)//2
            
            if(array[mid]!=array[mid+1] and array[mid]!=array[mid-1]):return array[mid]
            
            #left half element in right half so eliminate left half 
            
            if(( mid%2==1 and array[mid]==array[mid-1] ) or (mid%2==0 and array[mid]==array[mid+1])):
                left=mid+1
            else:
                right=mid-1
        return array[mid]
array=[1,1,2,2,3,3,4,5,5,6,6]
obj=solution()
result=obj.find_single_Element(array)
print(result)
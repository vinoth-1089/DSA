class solution:
    
    def three_sum(self,array):
        
        array.sort() 
        result=[]
        for i in range(len(array)):
            
            if i>0 and array[i]==array[i-1]:
                continue
            
            left=i+1
            right=len(array)-1
            
            while left<right:
                sum=array[i]+array[left]+array[right]
            
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    result.append([array[i],array[left],array[right]])
                    
                    while left<right and  array[left] == array[left+1]:
                        left+=1
                    while left<right and  array[right] == array[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result
    
array=[-1,0,1,2,-1,-4]
obj=solution()
print(obj.three_sum(array))
                
                
                
                
  
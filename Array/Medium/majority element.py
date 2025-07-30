class solution:
    
    # moore's voting algorithm
    def majority_element(self,array):
        
        element=None
        count=0
        
        for i in array:
            if count==0:
                element=i
                count=1
            elif i==element:
                count+=1
            else:
                count-=1
        if array.count(element)>len(array)//2:
            return element
        else:
            return "No majority element"
array=[2,2,2,1,1,1]
obj=solution()
print(obj.majority_element(array))
                 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
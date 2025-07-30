class solution:
    
    def remove_duplicate(self,array,n):
        
        i=0
        for j in range(1,n):
            if array[j]!=array[i]:
                array[i+1]=array[j]
                i+=1
        return array[:i+1]
array=[1,1,1,2,2,2,2,3]

n=len(array)
obj=solution()
print(obj.remove_duplicate(array,n))
class solution:
    
    def check_array(self,array,n):
        
        for i in range(1,n):
            if array[i]>=array[i-1]:
                pass
            else: 
                return False
        return True
array=[1,3,2,4,5]
n=len(array)
obj=solution()
print(obj.check_array(array,n))
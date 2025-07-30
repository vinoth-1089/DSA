class solution:
    def con_ones(self,array,n):
        
        current_lenght=0
        max_lenght=0
        
        for i in range(n):
            
            if array[i]==0:
                max_lenght=max(current_lenght,max_lenght)
                current_lenght=0
    
            else:
                current_lenght+=1
        return max(current_lenght,max_lenght)
array=[1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1]
n=len(array)
obj=solution()
print(obj.con_ones(array,n))                                                             
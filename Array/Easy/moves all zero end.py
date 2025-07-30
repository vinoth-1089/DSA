class solution:
    def zero_move(self,array,n):
        i=0
        for j in range(n):
            if(array[j]!=0):
                array[i],array[j]=array[j],array[i]
                i+=1
        return array
    
array=[1,2,3,4,0,6,0,8]
n=len(array)
obj=solution()
print(obj.zero_move(array,n))
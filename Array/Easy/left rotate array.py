class solution:
    def rotate(self,array,n):
        temp=array[0]
        array=array[1:]+[temp]
        return array
array=[1,2,3,4,5]
n=len(array)
obj=solution()
print(obj.rotate(array,n))
        
             
class solution():
    def inertion_sort(self,array,n):
        for i in range(1,n):
            current_value=array[i]
            j=i-1
            while j>=0 and array[j]>current_value:
                array[j+1]=array[j]
                j-=1
            array[j+1]=current_value
        return array
array=[67,34,69,58,45]
print("Before Sorted:")
print(array)
n=len(array)
obj=solution()
result=obj.inertion_sort(array,n)
print("After Sorted:")  
print(result)


                
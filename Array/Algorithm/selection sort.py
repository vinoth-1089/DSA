class solution():
    def selection_sort(self,array,n):
        for i in range(n-1):
            for j in range(i+1,n):
                if array[j]<array[i]:
                    array[i],array[j]=array[j],array[i]
        return array
array=[23,4,56,78,98]
print("Before Sorted:")
n=len(array)
obj=solution()
result=obj.selection_sort(array,n)
print("After Sorted:")
print(result)
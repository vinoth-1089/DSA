<<<<<<< HEAD
class solution:
    
    def Merge_sort(self,array):
        if len(array)<=1:
            return array
        
        n=len(array)//2
        left_half=array[:n]
        right_half=array[n:]
        
        self.Merge_sort(left_half)
        self.Merge_sort(right_half)
        
        i=j=k=0
      
        while i< len(left_half) and j< len(right_half):
          
            if left_half[i]< right_half[j]:
              array[k]=left_half[i]
              i+=1
            else:
                array[k]=right_half[j]
                j+=1
            k+=1
        while i< len(left_half):
                   
              array[k]=left_half[i]
              i+=1
              k+=1
        while j< len(right_half):
            
              array[k]=right_half[j]
              j+=1
              k+=1
            
        return array
array=[38,27,43,3,9,22,10]
print("Original Array:")
print(array)
obj=solution()
result=obj.Merge_sort(array)
print("Sorted Array:")
print(result)
=======
class solution:
    
    def Merge_sort(self,array):
        if len(array)<=1:
            return array
        
        n=len(array)//2
        left_half=array[:n]
        right_half=array[n:]
        
        self.Merge_sort(left_half)
        self.Merge_sort(right_half)
        
        i=j=k=0
      
        while i< len(left_half) and j< len(right_half):
          
            if left_half[i]< right_half[j]:
              array[k]=left_half[i]
              i+=1
            else:
                array[k]=right_half[j]
                j+=1
            k+=1
        while i< len(left_half):
                   
              array[k]=left_half[i]
              i+=1
              k+=1
        while j< len(right_half):
            
              array[k]=right_half[j]
              j+=1
              k+=1
            
        return array
array=[38,27,43,3,9,22,10]
print("Original Array:")
print(array)
obj=solution()
result=obj.Merge_sort(array)
print("Sorted Array:")
print(result)
>>>>>>> daf84cd7edad7e66253a7542968eef25d52d94cf
                
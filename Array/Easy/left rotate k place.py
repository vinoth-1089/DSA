class solution:
    def k_rotate(self,array,k,n):
        k=k%n
        rotate_part=array[:k]
        remain_part=array[k:]
        k_array=remain_part+rotate_part
        return k_array
    # def k2_rotate(self,array,k,n): 
    #     k=k%n
    #     rotate_part=array[:k]
    #     for i in range(k,n+1):
    #         array[i-k]=array[i-1]
    #     return array+rotate_part
    
    #optimal solution
    def k3_rotate(self,array,k,n):
        k=k%n
        rotate_part=list(reversed(array[:k]))
        remain_part=list(reversed(array[k:]))
        return list(reversed(rotate_part+remain_part))
        
            
array=[1,2,3,4]
k=4
n=len(array)
obj=solution()
print(obj.k_rotate(array,k,n))
print(obj.k3_rotate(array,k,n))
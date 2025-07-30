class solution:
    def second_large(self,array,n):
        large=array[0]
        second_large_num=-1
          
        for i in range(n):
            if array[i]>large:
                second_large_num=large
                large=array[i]
            elif array[i]<large and array[i]>second_large_num:
                second_large_num=array[i]
                
        return second_large_num
    def second_small(self,array,n):
        small=array[0]
        second_small_num=float('inf')
        for i in range(n):
            if(array[i]<small):
                second_small_num=small
                small=array[i]
            elif array[i]!=small and array[i]<second_small_num:
                second_small_num=array[i] 
        return second_small_num

array=[2,1]
n=len(array)
obj=solution()
print(obj.second_large(array,n))
print(obj.second_small(array,n))
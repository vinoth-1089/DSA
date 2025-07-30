class solution:
    
    def maxi_subarray_sum(self,array):
        
        current_sum=array[0]
        max_sum=array[0]
        end=start=temp_start=-1
        
        for i in range(1,len(array)):
            
            if array[i]>current_sum+array[i]:
                current_sum=array[i]
                temp_start=i
                
            else:
                current_sum+=array[i]

            if current_sum>max_sum:
                
                max_sum=current_sum
                start=temp_start
                end=i
        return [max_sum],array[start:end+1]

array=[-1,2,-3,4,-1,2,1,-5,4]
obj=solution()
print(obj.maxi_subarray_sum(array))
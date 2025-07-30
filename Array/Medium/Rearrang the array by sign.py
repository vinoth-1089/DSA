class solution:
    
    def rearrange_sign(self,array):
        ans=[0]*len(array)
        posindex=0
        negindex=1
        for i in range(0,len(array)):
            
            if array[i]>0:
                ans[posindex]=array[i]
                posindex+=2
            else:
                ans[negindex]=array[i]
                negindex+=2
           
        return ans
          
array=[3,1,-2,-5,2,-4]
obj=solution()
print(obj.rearrange_sign(array))
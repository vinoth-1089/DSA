class solution:
    
    def four_sum(self,array,target):
        
        array.sort()
        n=len(array)
        result=[]
        for i in range(n-3):
            
            for j in range(i+1,n-2):
                if j>i+1 and array[j]==array[j-1]:
                    continue
                left=j+1
                right=n-1
                
                while left<right:
                    
                    total=array[i]+array[j]+array[left]+array[right]
                    
                    if total<target:
                        left+=1
                    elif total>target:
                        right-=1
                    else:
                        result.append([array[i],array[j],array[left],array[right]])
                        
                        while left<right and array[left]==array[left-1]:
                            left+=1
                        while left<right and array[right]==array[right-1]:
                            right-=1
                            
                        right-=1
                        left+=1
        return result
array=[1,0,-1,0,-2,2]
target=0
obj=solution()
print(obj.four_sum(array,target))
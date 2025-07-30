class solution:
    def k_sum(self,array,k):
        
        n=len(array)
        sum_a=array[0]
        right=0
        left=0
        max_len=0
        while (right<n):
            while (left<=right and sum_a >k):
                sum_a-=array[left]  
                left+=1
            if (sum_a==k):
                max_len= max(max_len,right-left+1)
        
            right+=1
            if (right<n) :
                sum_a+=array[right]
        return max_len
array=[1,2,3,1,1,1,1]
k=3
obj=solution()
print(obj.k_sum(array,k))
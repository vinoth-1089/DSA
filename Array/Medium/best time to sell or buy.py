class solution:
    
    def stock(self,array):
        
        profit=0
        min_val=array[0]
        
        for i in range(1,len(array)):
            
            cost=array[i]-min_val
            profit=max(profit,cost)
            min_val=min(min_val,array[i])
            
        return profit
array=[2,3,2,5,1,7,8,3]
obj=solution()
print(obj.stock(array))
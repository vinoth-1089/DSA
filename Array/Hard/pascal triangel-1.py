class solution:
    
    def ncr(self,n,r):
        
        result=1
        
        for i in range(0,r):
            
            result=result*(n-i)//(i+1)
            # result=result//(i+1)
        
        return result
row=int(input("\n Enter a row:"))
column=int(input("\n Enter a column:"))
obj=solution()
print(obj.ncr(row-1,column-1))


# you give a row and column that index which elemnt that have return
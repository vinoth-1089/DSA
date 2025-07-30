class solution:
    
    def num_once(self,array): 
        xor=0
        n=len(array)
        for i in range(n):
            xor^=array[i]
            print(xor)
        return xor
            

array=[1,1,2,2,3,4,4]
obj=solution()
print(obj.num_once(array))
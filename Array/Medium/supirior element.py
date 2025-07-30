class solution:
    def leader(self,array):
          
        leaders=[]
        temp_leader=float('-inf')
          
        for i in range(len(array)-1,-1,-1):
                
            if array[i]>temp_leader:
                temp_leader=array[i]
                leaders.append(array[i])
        return leaders[::-1]
array=[16,17,4,3,5,2]
obj=solution()
print(obj.leader(array))
                
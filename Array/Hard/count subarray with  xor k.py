class solution:
    
    def count_subarray(self,array,k):
        
     
        hashmap={0:1}
        count=0
        prefix_xor=0
        
        for i in  array:
            prefix_xor^=i
            
            if (prefix_xor^k) in hashmap:
                count+=hashmap[prefix_xor^k]
            hashmap[prefix_xor]=hashmap.get(prefix_xor,0)+1
        return count
array=[4,2,2,6,4]
k=6
obj=solution()
print(obj.count_subarray(array,k))
            
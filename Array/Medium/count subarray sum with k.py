class solution:
    
    
    def count_subarray_sum(self,array,k):
        
        hashmap={0:1}
        prefix_sum=0
        count=0 
        
        for i in array:
            prefix_sum+=i

            if (prefix_sum-k) in hashmap:
                
                count+=hashmap[prefix_sum-k]
                
            hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
        return count
array=[1,2,3,4,5]
k=3
obj=solution()
print(obj.count_subarray_sum(array,k))
            
            
            
            
# sum_map = {1: 2}
# sum_map.get(1, 0) → 2
# sum_map.get(3, 0) → 0  # because 3 not in map


# Suppose prefix_sum = 4, and sum_map looks like this:

# sum_map = {0: 1, 3: 1}

# Then:

# sum_map.get(4, 0) + 1 → 0 + 1 = 1    get(keyvalue,defaultvalue)
# sum_map[4] = 1

# Now:

# sum_map = {0: 1, 3: 1, 4: 1}

# If later prefix_sum is 4 again:

# sum_map.get(4, 0) + 1 → 1 + 1 = 2
# sum_map[4] = 2

# Now:

# sum_map = {0: 1, 3: 1, 4: 2}


# ---

# Why use get()?

# To avoid errors when the key doesn’t exist yet.
# It’s a safe and compact way to do:

# if prefix_sum in sum_map:
#     sum_map[prefix_sum] += 1
# else:
#     sum_map[prefix_sum] = 1

# Using get() makes the code shorter and cleaner.
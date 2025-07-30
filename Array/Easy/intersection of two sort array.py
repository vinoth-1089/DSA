class solution:
    def intersection(self,array_a,array_b):
        i=0
        j=0
        result=[]
        while i<len(array_a) and j<len(array_b):
            if array_a[i]>array_b[j]:
                j+=1
            elif array_a[i]<array_b[j]:
                i+=1
            else:
                if not result or result[-1]!=array_a[i]:
                    result.append(array_a[i])
                i+=1
                j+=1   
        return result
array_a = [1, 2, 3, 4, 5] 
array_b = [1, 2,6, 7]

obj = solution()
print(obj.intersection(array_a, array_b))

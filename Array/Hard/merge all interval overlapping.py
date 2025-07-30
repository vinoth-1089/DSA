class solution:
    
    
    def merge_interval(self,intervals):
        
        if not intervals:
            return []
         
        intervals.sort(key=lambda x: x[0])
        merge=[intervals[0]]
        
        for current in intervals[1:]:
            last=merge[-1]
            
            if current[0] <= last[1]:
                
                last[1]=max(last[1],current[1])
            else:
                merge.append(current)
        return merge
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
obj=solution()
print(obj.merge_interval(intervals))       

def binary_search_first_occurarence(arr,target):
    
    left=0
    right=len(arr)-1
    first=-1
    while(left<=right):
        mid=left+(right-left)//2
        if arr[mid]==target:
            first=mid
            right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return first
            
def binary_search_last_occurarence(arr,target):
        left=0
        right=len(arr)-1
        second=-1
        while(left<=right):
            mid=left+(right-left)//2
            if arr[mid]==target:
                second=mid
                left=mid+1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return second
        
array=[2,2,2,4,5,6,7,8]
target=2
first=binary_search_first_occurarence(array,target)
last=binary_search_last_occurarence(array,target)
if first != -1 and first == last:
    last = -1

print((first, last))
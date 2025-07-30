def sort012(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        mid=(left+right)//2
        if arr[mid]>=arr[mid+1]:
            arr[mid],arr[mid+1]=arr[mid+1],arr[mid]
        else:
            continue
           
arr=[0,1,2,0,2]
print(sort012(arr))        
            
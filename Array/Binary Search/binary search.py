arr=[1,2,3,4,5,6]
left=0
right=len(arr)-1
target=int(input("Enter the target:"))

while(left<right):
    mid=left+(right-left)//2

    if arr[mid]==target:
        print(mid)
    elif arr[mid]<target:
        right=mid-1
    else:
       left=mid+1
    print(mid)
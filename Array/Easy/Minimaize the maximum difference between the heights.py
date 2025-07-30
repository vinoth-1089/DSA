def maxidifference(arr,k):

    n=len(arr)
    arr1=[]

    for i in range(n):
        if k<arr[i]:
           g=arr[i]-k
           arr1.append(g)
        # elif k==arr[i]:
        #     g=k+arr[i]
        #     arr1.append(g)
        else:
            g=arr[i]+k
            arr1.append(g)
        
        if arr[i]-k<0:
            continue
        minh=min(arr1[0]+k,arr1[i]-k)
        maxh=max(arr1[i-1]+k,arr1[n-1]-k)
        res=min(maxh-minh)

#         return res

arr=[12,6,4,15,17,10]
k=6
b=0
print(maxidifference(arr,k))

        

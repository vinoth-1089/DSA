def mini(arr,dep,n):
    platform_need=1
    result=1

    for i in range(n):
         
        platform_need=1
        for j in range(n):
            if i!=j:
                if(arr[i]>=arr[j] and dep[j]>=arr[i]):
                    platform_need+=1
        result=max(result,platform_need)
    return result
arr=[100,300,500]
dep=[900,400,600]
n=len(arr)
print(mini(arr,dep,n))
            




def minimum(arr,dep,n):

    arr.sort()
    dep.sort()
    platform_need=1
    result=1

    i=1
    j=0
    while(i<n and j<n):
        if(arr[i]<=dep[j]):
            platform_need+=1
            i+=1
        elif(arr[i]>dep[j]):
            platform_need-=1
            j+=1
        if(platform_need>result):
            result=platform_need
    return result





arr=[100,300,500]
dep=[900,400,600]
n=len(arr)
print(minimum(arr,dep,n))           
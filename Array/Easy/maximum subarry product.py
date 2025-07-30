def maximumpro(arr,n):
    result=arr[0]

    for i in range(n):
        mul=1
        for j in range(i,n):
            mul*=arr[j]
            result=max(result,mul)
    return result
arr=[-2,6,-3,-10,0,2]
n=len(arr)
print(maximumpro(arr,n))
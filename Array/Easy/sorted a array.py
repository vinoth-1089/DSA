def bubble(arr):

    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):

           if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

arr=[170,45,75,90,802,24,2,66]
bubble(arr)
               



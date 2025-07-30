def listed(a,start,end):
    while(start<end):
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
a=[1,2,3,4,5]

print(a)
listed(a,0,len(a)-1)
print(a)


def usingstack(arr):
    stack=[]

    for i in arr:
        stack.append(i)

    for j in range(len(arr)):
        arr[j]=stack.pop()
    
arr=[1,2,4,5]
usingstack(arr)
print(arr)


def extraarray(arr2):
    a=arr2[::-1]

for i in a:
    print(i,end=" ")

arr3=[1,2,3,4,5,6]
extraarray(arr3)
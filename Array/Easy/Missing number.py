class solution:
    #optimal-1
    def missing(self,num):
        l=len(num)+1
        s=sum(num)
        m=l*(l+1)//2
        mis=m-s
        return mis
    def best(self,num):
        xor1=0
        xor2=0
        n=len(num)-1
        for i in range(0,n):
            xor2^=num[i]
            xor1^=(i+1)
           
        xor1=xor1^len(num) #reaming value
        return xor1^xor2
obj=solution()
num=[1,2,3,5]

print(obj.missing(num))
print(obj.best(num))

# n=int(input("\n Enter a expected length:"))
# arr=[int(i) for i in input("\n ENter a number:")for i in range(n-1):]#range your choice
# total=n*(n+1)//2-sum(arr)
# print(total)
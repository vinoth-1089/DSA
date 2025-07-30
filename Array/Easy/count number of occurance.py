arr=[int(i) for i in input("Enter the value:").split(",")]
target=int(input("enter the target:"))
c=0
for i in arr:
    if i==target:
        c+=1
print(c)
n=input().split(" ")
k=int(input("Enter the k value:"))

for i in n:
    if len(i)>=k:
        result=i[-k:]
print(result[::-1],end=" ")
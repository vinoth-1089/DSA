n=[1,3,5,26,4]
for i in range(0,len(n)-1):
    for j in range(0,len(n)-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)

print("-------------------------------------")

# n=[1,3,5,26,4]
# while(True):
#     a=True
#     for j in range(0,len(n)-1):
#         if n[j]>n[j+1]:
#             n[j],n[j+1]=n[j+1],n[j]
#         a=False
#     if a==True:
#         break
# print(n)

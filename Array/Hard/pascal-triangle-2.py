class solution:
    
    
    def pascal_triangle(self,row):
        
        answer=1
        print(answer)
        for col in range(1,row):
            
            answer=answer*(row-col)//col
            print(answer)
            
row=int(input("\n Enter a row:"))
obj=solution()
obj.pascal_triangle(row)
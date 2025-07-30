class solution:
    def pascal_triangle(self,row):
        for row in range(row):
            answer = 1
            temp = [1]  # First value of each row is always 1
            for col in range(1, row+ 1):
                answer = answer * (row - col+1) // col
                temp.append(answer)
            print(temp)
            
row=int(input("\n Enter a row:"))
obj=solution()
obj.pascal_triangle(row)